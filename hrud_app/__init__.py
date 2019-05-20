import os
from flask import Flask, redirect, url_for, render_template


def create_app(test_config=None, config_file_name="./settings.py"):
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

    from hrud_app.model import db
    db.init_app(app)

    from hrud_app.views import api
    api.init_app(app)

    from hrud_app.views import pages
    app.register_blueprint(pages)

    @app.route('/', defaults={'path': ''})
    def index():
        return render_template("index.html")

    return app

# END OF FILE

