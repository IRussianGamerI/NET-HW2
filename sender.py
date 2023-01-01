import time
import requests
import logging

from db_fetcher import fetch_pending

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] => [%(message)s]"
)

logger = logging.getLogger(__name__)


def send_to_producer():
    # Call the gosuslugi function to get the data
    data = fetch_pending()

    # Send the data to the Kafka producer
    for d in data:
        requests.post("http://localhost:8080/produce", json=d)
        logger.info(f"{d} sent to producer")


if __name__ == "__main__":
    while True:
        send_to_producer()
        # Sleep for 5 seconds before checking the database again
        time.sleep(5)
