import datetime
from typing import Any

import pymysql
from sqlalchemy import ForeignKey, MetaData, String, DateTime, create_engine, Column, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, sessionmaker


metadata_obj = MetaData()


class Base(DeclarativeBase):
    pass


class CarPrices(Base):
    __tablename__ = "cars_price_info"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_car_model = Column("id_car_model", ForeignKey("cars_model_info.id"))
    price = Column("price", Float)
    date_added = Column("date_added", DateTime)

    def __init__(self, id_car_model: int, price: float, date_added: datetime, **kw: Any):
        super().__init__(**kw)
        self.id_car_model = id_car_model
        self.price = price
        self.date_added = date_added


class Cars(Base):
    __tablename__ = "cars_model_info"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    model = Column("model", String(30))
    manufacturer = Column("manufacturer", String(30))

    def __init__(self, model: str, manufacturer: str, **kw: Any):
        super().__init__(**kw)
        self.model = model
        self.manufacturer = manufacturer


class Report(Base):
    __tablename__ = "report_info"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    median = Column("median", Float)
    lowest_price = Column("lowest_price", Float)
    highest_price = Column("highest_price", Float)
    day_of_lowest_price = Column("day_of_lowest_price", DateTime)
    day_of_highest_price = Column("day_of_highest_price", DateTime)
    sent = Column("sent", Boolean)
    sent_date = Column("sent_date", DateTime)

    def __init__(self, median: float, lowest_price: float, highest_price: float, day_of_lowest_price: datetime, day_of_highest_price: datetime, sent: bool, sent_date: datetime, **kw: Any):
        super().__init__(**kw)
        self.median = median
        self.lowest_price = lowest_price
        self.highest_price = highest_price
        self.day_of_lowest_price = day_of_lowest_price
        self.day_of_highest_price = day_of_highest_price
        self.sent = sent
        self.sent_date = sent_date


engine = create_engine("mysql+pymysql://root@localhost/monthly_report", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
