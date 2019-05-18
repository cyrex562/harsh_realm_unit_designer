"""
settings.py



"""
import os

DEBUG = True
TESTING = False
SECRET_KEY = os.urandom(24)
VERSION = "0.1"
MONGODB_SETTINGS = {
        "db": os.environ["MONGO_DB_NAME"],
        "host": os.environ["MONGO_HOST"],
        "port": 27017,
        "username": os.environ["MONGO_USER"],
        "password": os.environ["MONGO_PASSWORD"]
}

# END OF FILE
