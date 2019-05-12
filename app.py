from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restplus import Api

db = MongoEngine()
api = Api()


def create_app(config_file_name: str):
    app = Flask(__name__)
    app.config.from_object(config_file_name)

    # init database and other plugins
    db.init_app(app)
    api.init_app(app)

    # import blueprints
    from views import pages_app

    # register blueprints
    app.register_blueprint(pages_app)

    return app

# END OF FILE
