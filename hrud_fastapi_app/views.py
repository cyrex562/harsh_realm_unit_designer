import uuid

from flask import Blueprint, render_template, current_app, redirect, request
from flask_restplus import Api, Resource, fields

from hrud_app import settings
from hrud_app import model
api = Api(doc="/doc/")

pages = Blueprint('pages',
                  __name__,
                  template_folder='templates',
                  url_prefix='/pages',
                  static_folder='static')


@pages.route('/')
def def_pages_route():
    return render_template('index.html', version=settings.VERSION)


unit_api_model = api.model('Unit',
                           {
                               "hq_unit": fields.Boolean,
                               "name": fields.String
                           })


@api.route('/units')
class UnitResource(Resource):
    def get(self):
        units = []
        for unit in model.Unit.objects():
            units.append(unit.to_mongo())
        return {"units": units}, 200

    @api.marshal_with(unit_api_model, code=201)
    def post(self):
        req_json = request.json
        req_form = request.form
        data = api.payload
        is_hq_unit = data.get("hq_unit", False)
        name = data.get("name", "")
        # TODO: role codes
        # TODO: identifier
        # TODO: assets
        # TODO: effects
        # TODO: abilities
        unit = model.Unit(uuid=uuid.uuid4(),
                          hq_unit=is_hq_unit,
                          name=name,
                          )
        unit.save()


@api.route('/unit/<string:uint_id>')
class SingleUnitResource(Resource):
    def get(self, unit_id):
        matching_unit = model.Unit.objects(identifier=unit_id)
        if matching_unit is not None and len(matching_unit) > 0:
            matching_unit = matching_unit[0].to_mongo()
            return {"unit": matching_unit}, 200
        else:
            return {"message": "no matching unit found"}, 404



# END OF FILE
