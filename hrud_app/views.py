import uuid
from flask import Blueprint, render_template, current_app, redirect, request
from flask_admin.contrib.appengine import ModelView

from hrud_app import settings
from hrud_app import model

pages = Blueprint('pages',
                  __name__,
                  template_folder='templates',
                  url_prefix='/',
                  static_folder='static')

@pages.route('/')
def def_pages_route():
    return render_template('index.html', version=settings.VERSION)


class RoleCodeView(ModelView):
    column_filters = ["role"]

    # column_searchable_list = ["role"]

    form_ajax_refs = {
            "tags": {
                    "fields": ("role",)
            }
    }


class UnitAssetView(ModelView):
    column_filters = ["name"]
    # column_searchable_list = ()
    form_ajax_refs = {
            "tags": {
                    "fields": ("name",)
            }
    }

class UnitEffectView(ModelView):
    column_filters = ["name"]
    # column_searchable_list = ()
    form_ajax_refs = {
            "tags": {
                    "fields": ("name",)
            }
    }

class UnitView(ModelView):
    column_filters = ['hq_unit', 'is_hq',]

# END OF FILE
