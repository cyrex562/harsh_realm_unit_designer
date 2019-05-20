"""
settings.py

Flask settings file

"""
import os

DEBUG = True
TESTING = False
SECRET_KEY = os.urandom(24)
VERSION = "0.1"
# pull sensitive settings data from environment variables set at app launch time.
MONGODB_SETTINGS = {
        "db": os.environ["MONGO_DB_NAME"],
        "host": os.environ["MONGO_HOST"],
        "port": 27017,
        # "username": os.environ["MONGO_USER"],
        # "password": os.environ["MONGO_PASSWORD"]
}

SWAGGER_UI_OPERATION_ID = True
SWAGGER_UI_REQUEST_DURATION = True
SWAGGER_UI_DOCK_EXPANSION = 'full'

# END OF FILE
