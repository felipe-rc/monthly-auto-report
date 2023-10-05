import datetime
from model import ORMconfig


def create_car(model: str, manufacturer: str):
    new_car = ORMconfig.Cars(model, manufacturer)
    ORMconfig.session.add(new_car)
    ORMconfig.session.commit()


def list_cars():
    return ORMconfig.session.query(ORMconfig.Cars).all()


def list_car_by_id(idIn: int):
    return ORMconfig.session.query(ORMconfig.Cars).filter(ORMconfig.Cars.id == idIn)


def insert_car_price(car: ORMconfig.Cars, price: float):
    new_car_price = ORMconfig.CarPrices(car.id, price, datetime.date.today())
    ORMconfig.session.add(new_car_price)
    ORMconfig.session.commit()


def list_car_prices():
    return ORMconfig.session.query(ORMconfig.CarPrices).all()


def list_car_prices_by_car_id(car_id: int):
    return ORMconfig.session.query(ORMconfig.CarPrices).filter(ORMconfig.CarPrices.id_car_model == car_id)


def create_report(median: float, lowest_price: float, highest_price: float, day_of_lowest_price, day_of_highest_price):
    new_report = ORMconfig.Report(median, lowest_price, highest_price, day_of_lowest_price, day_of_highest_price, True, datetime.date.today())
    ORMconfig.session.add(new_report)
    ORMconfig.session.commit()
