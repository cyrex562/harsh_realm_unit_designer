import os

from flask import Flask, render_template
from flask_admin import Admin


def create_app(test_config=None, config_file_name="./settings.py"):
    """

    Args:
        test_config:
        config_file_name:

    Returns:

    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    # check if we're using a test configuration or a configuration file
    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile(config_file_name)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # flask-admin
    admin = Admin(app, name="harsh-realm", template_mode='bootstrap4')
    # add admin views here

    # db app
    from hrud_app.model import db
    db.init_app(app)

    # views blueprints
    from hrud_app.views import pages
    app.register_blueprint(pages)

    return app

# END OF FILE

