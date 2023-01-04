import json
from abc import ABC

import mysql.connector
import tornado.ioloop
import tornado.web


class UpdateStatusHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="dbuser",
            password="123",
            database="net-hw2"
        )
        cursor = connection.cursor()

        # Get the notification ID and new status from the request body
        data = json.loads(self.request.body)
        notification_id = data["notification_id"]
        new_status = data["new_status"]

        # Update the notification status in the database
        cursor.execute("UPDATE notifications SET status = %s WHERE id = %s", (new_status, notification_id))
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()


def make_app():
    return tornado.web.Application([
        (r"/update_status", UpdateStatusHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(7999)
    tornado.ioloop.IOLoop.current().start()
