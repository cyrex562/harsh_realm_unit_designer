import os
from typing import List

import uuid as uuid
from fastapi import FastAPI

from hrud_fastapi_app import model
from mongoengine import connect

from pydantic import BaseModel, UUID4


class Unit(BaseModel):
    # is hq unit
    is_hq: bool = False
    # hq unit
    hq_unit: str = ""
    # unit role
    role_codes: List[str] = None
    # supported units
    supported_units: List[str] = None
    # name
    name: str = ""
    # id code
    id_code: str = ""


app = FastAPI()

connect(db=os.environ["MONGO_DB"], host=os.environ["MONGO_HOST"])

@app.get("/")
# for now not using async as recommended in the docs:
#     https://fastapi.tiangolo.com/async/#in-a-hurry
def root():
    return {"message": "hello world"}


@app.get("/api/units")
def read_units():
    units = []
    for unit in model.Unit.objects():
        units.append(unit.to_mongo())
    return {"units": units}, 200

@app.post("/api/units")
def create_unit(unit: Unit):

    return unit

