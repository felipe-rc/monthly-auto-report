import datetime

import ORMconfig
from sqlalchemy import update


def create_car(model: str, manufacturer: str):
    new_car = ORMconfig.Cars(model, manufacturer)
    ORMconfig.session.add(new_car)
    ORMconfig.session.commit()
