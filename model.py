"""
:file: model.py
"""
from mongoengine import UUIDField, Document, BooleanField, ListField, IntField, \
    StringField


class Unit(Document):
    uuid = UUIDField(binary=False)
    # hq unit
    hq_unit = StringField()
    # is hq
    is_hq = BooleanField(default=False)
    # unit role
    role_codes = ListField(field=IntField)
    # supported units
    supported_units = ListField(field=StringField)
    # unit name
    name = StringField()
    # unit identifier
    identifier = StringField()
    # unit assets
    assets = ListField(field=StringField)
    # unit effects
    effects = ListField(field=StringField)
    # unit abilities
    abilities = ListField(field=StringField)