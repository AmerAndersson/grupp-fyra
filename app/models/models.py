import datetime
from app.db import *
from sqlalchemy import Column, Integer, String
from sqlalchemy import DECIMAL, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class CustomerCar(Base):
    __tablename__ = 'customerCar'

    customerCar_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(String(7), nullable=False, unique=True)
    brand = Column(String(50), nullable=False)
    car_model = Column(String(50), nullable=False)
    car_color = Column(String(50), nullable=False)
    year_model = Column(DateTime, default=datetime.datetime.utcnow())
    customerCar = relationship('CustomerCarHasProducts', back_populates='product')


class Customers(Base):
    __tablename__ = 'customers'

    customers_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50), nullable=False, unique=True)
    product_number = Column(String(50), nullable=False, unique=True)
    product_vendor = Column(String(50), nullable=False)
    product_description = Column(String(255), nullable=False)
    quantityin_stock = Column(Integer, nullable=False, unsigned=True)
    buy_price = Column(DECIMAL(10.0), nullable=False)
    product = relationship('CustomerCarHasProducts', back_populates='customerCar')


class CustomerCarHasProducts(Base):
    __tablename__ = 'customerCar_has_products'

    product_id = Column(ForeignKey('products.product_id'), primary_key=True)
    customers_id = Column(ForeignKey('customers.customer_id'), primary_key=True)
    customerCar = relationship('CustomerCar', back_populates='product')
    product = relationship('Products', back_populates='customerCar')