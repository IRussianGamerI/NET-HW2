class Config:
    pass


config = Config()
config.SERVER = 'localhost:9092'
config.TOPIC = 'net-hw2'
config.MAX_TRIES = 5
# config.TOKEN = "write your token here"  # You must get it from VK. It must have access to messages API
config.VK_API_VERSION = "5.131"
