class Config:
    pass


config = Config()
config.SERVER = '127.0.0.1:9092'
config.TOPIC = 'kafkadz'
config.MAX_TRIES = 5
# config.TOKEN = "write your token here"  # You must get it from VK. It must have access to messages API
config.VK_API_VERSION = "5.131"
