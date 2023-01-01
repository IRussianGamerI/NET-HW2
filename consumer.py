from kafka import KafkaConsumer
import json
import requests
import time
import logging

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
    for msg in consumer:
        print(msg.value)
        print(msg.value['user_id'])
        user_id = msg.value['user_id']
        message = msg.value['date'] + ' ' + msg.value['msg']

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

        if not success:
            logger.error("Передача в календарь сообщения об ошибке")

    consumer.poll()
