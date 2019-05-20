"""
model.py

Models specification for the app.

"""
from flask_mongoengine import MongoEngine
from mongoengine import UUIDField, Document, BooleanField, ListField, IntField, \
    StringField, ReferenceField

db = MongoEngine()


class RoleCode(Document):
    role = StringField()


class UnitAsset(Document):
    name = StringField()


class UnitEffect(Document):
    name = StringField()


class UnitAbility(Document):
    name = StringField()


class Unit(Document):
    """
    Unit specification
    """
    uuid = UUIDField(binary=False)
    # hq unit
    hq_unit = ReferenceField('self')
    # is hq
    is_hq = BooleanField(default=False)
    # unit role
    role_codes = ListField(ReferenceField(RoleCode))
    # supported units
    supported_units = ListField(ReferenceField('self'))
    # unit name
    name = StringField()
    # unit identifier
    identifier = StringField()
    # unit assets
    assets = ListField(ReferenceField(UnitAsset))
    # unit effects
    effects = ListField(ReferenceField(UnitEffect))
    # unit abilities
    abilities = ListField(ReferenceField(UnitAbility))
