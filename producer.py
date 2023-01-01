import json
import time
import logging

from kafka import KafkaProducer

from config import config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] => %(message)s",
)

logger = logging.getLogger(__name__)


def gosuslugi():
    return [
        {"user_id": "242217382", "date": "2022-12-04 20:00:00", "msg": 'У вас неоплаченная налоговая задолженность'},
        {"user_id": "242217382", "date": "2022-12-05 20:00:00", "msg": 'У вас новый штраф! Оплатите в течение 5 дней'},
        {"user_id": "242217382", "date": "2022-12-06 20:00:00", "msg": 'Ваш загранпаспорт готов к выдаче'},
        {"user_id": "242217382", "date": "2022-12-07 20:00:00", "msg": 'Открыта запись на ДЭГ в 2022 году'},
        {"user_id": "242217382", "date": "2022-12-08 20:00:00", "msg": "Узнайте, как получить субсидию на ремонт"}]


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=[config.SERVER],
                             value_serializer=lambda m: json.dumps(m).encode())

    notifications = gosuslugi()
    print(len(notifications))

    for note in notifications:
        producer.send(config.TOPIC, value=note)
        logger.info(f"{note} sent to consumer")
        time.sleep(5)

    producer.flush()
