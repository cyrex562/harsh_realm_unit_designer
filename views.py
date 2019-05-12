from flask import Blueprint, render_template

import settings

pages_app = Blueprint('pages_app', __name__)

@pages_app.route('/')
def index():
    return render_template('index.html', version=settings.VERSION)