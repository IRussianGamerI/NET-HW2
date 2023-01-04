import time
import requests
import logging

import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] => [%(message)s]"
)

logger = logging.getLogger(__name__)


def fetch_pending():
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="dbuser",
        password="123",
        database="net-hw2"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT ID, vk_id, date, msg FROM notifications WHERE status = 'pending'")
    rows = cursor.fetchall()

    # Format the data as a list of dictionaries
    data = []
    for row in rows:
        data.append({
            "notification_id": row[0],
            "user_id": row[1],
            "date": str(row[2]),
            "msg": row[3]
        })

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return data


def send_to_producer():
    # Call the gosuslugi function to get the data
    data = fetch_pending()

    # Send the data to the Kafka producer
    for d in data:
        requests.post("http://localhost:7999/update_status", json={
            "notification_id": d["notification_id"],
            "new_status": "processing"
        })
        requests.post("http://localhost:8000/produce", json=d)
        logger.info(f"{d} sent to producer")


if __name__ == "__main__":
    while True:
        try:
            send_to_producer()
            # Sleep for 30 seconds before checking the database again
            time.sleep(30)
        except KeyboardInterrupt:
            print("Sender is shutting down")
            break
