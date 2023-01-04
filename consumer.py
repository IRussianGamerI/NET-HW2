import json
import requests
import time
import logging

from kafka import KafkaConsumer

from config import config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] => %(message)s",
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    consumer = KafkaConsumer(config.TOPIC,
                             bootstrap_servers=[config.SERVER],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    try:
        for msg in consumer:
            logger.info(msg.value)
            user_id = msg.value['user_id']
            message = msg.value['date'] + '\n' + msg.value['msg']
            notification_id = msg.value['notification_id']

            success = False

            for try_iter in range(config.MAX_TRIES):
                try:
                    url = f"https://api.vk.com/method/messages.send?user_id={user_id}&message={message}&" \
                          f"random_id={int(time.time())}&access_token={config.TOKEN}&v={config.VK_API_VERSION}"

                    r = requests.post(url)
                    logger.info(r)
                    success = True
                    time.sleep(5)
                    break
                except:
                    logger.warning("Ошибка сети")
                    time.sleep(1)

            if success:
                # Send HTTP POST request to `sender.py` to update the notification's status to "sent"
                requests.post("http://localhost:7999/update_status", json={
                    "notification_id": notification_id,
                    "new_status": "sent"
                })
            else:
                logger.info("Превышено количество попыток отправки")
                # Send HTTP POST request to `sender.py` to update the notification's status to "failed"
                requests.post("http://localhost:7999/update_status", json={
                    "notification_id": notification_id,
                    "new_status": "failed"
                })

    except KeyboardInterrupt:
        logger.info("Consumer is shutting down...")
    finally:
        consumer.close()
