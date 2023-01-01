import json
import logging
import tornado.ioloop
import tornado.web

from kafka import KafkaProducer

from config import config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] => %(message)s",
)

logger = logging.getLogger(__name__)

producer = KafkaProducer(bootstrap_servers=[config.SERVER],
                         value_serializer=lambda m: json.dumps(m).encode())


class ProduceHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        producer.send(config.TOPIC, value=data)
        logger.info(f"{data} sent to consumer")


def make_app():
    return tornado.web.Application([
        (r"/produce", ProduceHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
