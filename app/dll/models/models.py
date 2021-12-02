import datetime
from app.dll.db import *
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
    customerCar = relationship('CustomersHasCustomerCar', back_populates='customer_has_car')


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
    customers = relationship('CustomersHasCustomerCar', back_populates='customer')
    employee_id = Column(ForeignKey('customers.employee_id'))
    customer = relationship('Employees', back_populates='employee_customer')
    order = relationship('Order', back_populates='customer')


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    reseller_id = Column(ForeignKey('reseller.reseller_id'), primary_key=True)
    product_name = Column(String(50), nullable=False, unique=True)
    product_number = Column(String(50), nullable=False, unique=True)
    product_vendor = Column(String(50), nullable=False)
    product_description = Column(String(255), nullable=False)
    quantityin_stock = Column(Integer, nullable=False, unsigned=True)
    buy_price = Column(DECIMAL(10.0), nullable=False)
    products = relationship('CustomerCarHasProducts', back_populates='customerCar')
    products_details = relationship('OrderDetails', back_populates='order_details')
    product = relationship('Reseller', back_populates='resellers')


class CustomerCarHasProducts(Base):
    __tablename__ = 'customerCar_has_products'

    product_id = Column(ForeignKey('customerCar_has_products.product_id'), primary_key=True)
    customerCar_id = Column(ForeignKey('customerCar_has_products.customerCar_id'), primary_key=True)
    customerCar = relationship('Products', back_populates='products')


class CustomersHasCustomerCar(Base):
    __tablename__ = 'customers_has_customerCar'

    customers_id = Column(ForeignKey('customers_has_customerCar.customers_id'), primary_key=True)
    customerCar_id = Column(ForeignKey('customers_has_customerCar.customers_id'), primary_key=True)
    customer_has_car = relationship('CustomerCar', back_populates='customerCar')
    customer = relationship('Customers', back_populates='customers')


class Offices(Base):
    __tablename__ = 'offices'

    offices_id = Column(Integer, primary_key=True, autoincrement=True)
    offices_code = Column(Integer)
    offices_name = Column(String(50), nullable=False)
    offices_address = Column(String(50), nullable=False)
    offices_number = Column(String(50), nullable=False)
    contact_employee = Column(String(50), nullable=False)
    employee_name = Column(String(50), nullable=False)
    employee_phone_number = Column(String(50), nullable=False)
    employee_email = Column(String(50), nullable=False)
    employee = relationship('Employees', back_populates='offices')


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(50), nullable=False)
    offices_id = Column(ForeignKey('employees.offices_id'))
    offices = relationship('Offices', back_populates='employee')
    employee_customer = relationship('Customers', back_populates='customer')


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=datetime.datetime.utcnow())
    shipping_date = Column(DateTime, default=datetime.datetime.utcnow())
    status = Column(String(50), nullable=False)
    customers_id = Column(ForeignKey('order.customers_id'), primary_key=True)
    customer = relationship('Customers', back_populates='order')


class OrderDetail(Base):
    __tablename__ = 'orderDetail'

    order_order_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(ForeignKey('orderDetail.product_id'), primary_key=True)
    order_id = Column(ForeignKey('orderDetail.order_id'), primary_key=True)
    quantity_order = Column(Integer)
    price_each = Column(DECIMAL(10.0))
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    order_details = relationship('Products', back_populates='products_details')


class Reseller(Base):
    __tablename__ = 'reseller'

    reseller_id = Column(Integer, primary_key=True, autoincrement=True)
    reseller_name = Column(String(50), nullable=False)
    reseller_address = Column(String(50), nullable=False)
    reseller_contact_person = Column(String(50), nullable=False)
    reseller_phone_number = Column(String(50), nullable=False)
    reseller_email = Column(String(50), nullable=False)
    manufacturer_id = Column(ForeignKey('reseller.manufacturer_id'), primary_key=True)
    reseller = relationship('Manufacturer', back_populates='manufacturer')
    resellers = relationship('Products', back_populates='product')


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(50), nullable=False)
    manufacturer = relationship('Manufacturer', back_populates='reseller')