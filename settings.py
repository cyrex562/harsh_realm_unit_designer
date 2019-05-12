import os

DEBUG = True
TESTING = False
SECRET_KEY = os.urandom(24)
VERSION = "0.1"
MONGODB_SETTINGS = {
        "db": "harsh_realm_unit_designer",
        "host": "192.168.122.11",
        "port": 27017,
        "username": "admin",
        "password": "azazel56"
}