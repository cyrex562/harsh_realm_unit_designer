from flask import Flask


def create_app(config_file_name: str):
    app = Flask(__name__)
    app.config.from_object(config_file_name)

    # init database and other plugins

    # import blueprints
    from views import pages_app

    # register blueprints
    app.register_blueprint(pages_app)

    return app

# END OF FILE
