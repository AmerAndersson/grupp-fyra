import datetime
<<<<<<< HEAD
from app.src.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import DECIMAL, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class CustomersHasCustomerCar(Base):
    __tablename__ = 'customers_has_customerCar1'

    customerCar_customerCar_id = Column(Integer, ForeignKey('customerCars.customerCar_id'), primary_key=True)
    customers_customers_id = Column(Integer, ForeignKey('customers.customers_id'), primary_key=True)
    car = relationship('CustomerCars', back_populates='customers_cars')
    owner_car = relationship('Customers', back_populates='customers_has_car')

    def __repr__(self):
        return f'{self.car} {self.owner_car}'


class CustomerCarHasProducts(Base):
    __tablename__ = 'customerCars_has_products'

    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    customerCars_customerCar_id = Column(Integer, ForeignKey('customerCars.customerCar_id'), primary_key=True)
    product_has_products = relationship('Products', back_populates='product_has_cars')
    customerCar_has_products = relationship('CustomerCars', back_populates='cars_has_products')

    def __repr__(self):
        return f'{self.product_has_products} {self.customerCar_has_products}'


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100), nullable=False, unique=True)
    product_number = Column(String(100), nullable=False, unique=True)
    product_vendor = Column(String(100), nullable=False)
    product_description = Column(String(255), nullable=False)
    quantityin_stock = Column(Integer, nullable=False)
    buy_price = Column(DECIMAL(10, 2), nullable=False)
    resellers_reseller_id = Column(Integer, ForeignKey('resellers.reseller_id'), primary_key=True)
    resellers = relationship('Resellers', back_populates='products')
    orders = relationship('Orders', back_populates='product')
    product_has_cars = relationship('CustomerCarHasProducts', back_populates='product_has_products')

    def __repr__(self):
        return f"""
        ProductsID:  {self.product_id}
        ProductName: {self.product_name}
        ProductNumber: {self.product_number}
        ProductVendor: {self.product_vendor}
        ProductDescription: {self.product_description}
        QuantityInStock: {self.quantityin_stock}
        BuyPrice: {self.buy_price}
        """


class Customers(Base):
    __tablename__ = 'customers'

    customers_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    zip_code = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    employees_employee_id = Column(Integer, ForeignKey('employees.employee_id'), primary_key=True)
    employee = relationship('Employees', back_populates='customers')
    order = relationship('Orders', back_populates='customer')
    customers_has_car = relationship('CustomersHasCustomerCar', back_populates='owner_car')

    def __repr__(self):
        return f"""
        CustomersID: {self.customers_id}
        Fullname: {self.first_name} {self.last_name}
        Address: {self.address}
        Phone: {self.phone}
        Email: {self.email} 
        City: {self.city}
        ZipCode: {self.zip_code} 
        Country: {self.country} 
        Customers_has_car: {self.customers_has_car} 
        """


class CustomerCars(Base):
    __tablename__ = 'customerCars'

    customerCar_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(String(7), nullable=False)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    color = Column(String(50), nullable=False)
    years = Column(DateTime, default=datetime.datetime.utcnow)
    customers_cars = relationship('CustomersHasCustomerCar', back_populates='car')
    cars_has_products = relationship('CustomerCarHasProducts',  back_populates='customerCar_has_products')

    def __repr__(self):
        return f"""
        RegisterNumber: {self.reg_number}
        CarBrand: {self.brand}
        CarModel: {self.model}
        CarColor: {self.color} 
        YearMade: {self.years}
         """


class Offices(Base):
    __tablename__ = 'offices'

    offices_id = Column(Integer, primary_key=True, autoincrement=True)
    offices_code = Column(Integer)
    offices_name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    employee_name = Column(String(100), nullable=False)
    employee_phone = Column(String(100), nullable=False)
    employee_email = Column(String(100), nullable=False)
    employee = relationship('Employees', back_populates='offices')

    def __repr__(self):
        return f"""
        OfficesID: {self.offices_id}
        OfficesCode: {self.offices_code} 
        OfficesName: {self.offices_name} 
        Addresses: {self.address} 
        Phone: {self.phone}
        EmployeesName: {self.employee_name} 
        EmployeesPhone: {self.employee_phone} 
        EmployeesEmail: {self.employee_email}
        """


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    offices_offices_id = Column(Integer, ForeignKey('offices.offices_id'), primary_key=True)
    offices = relationship('Offices', back_populates='employee')
    customers = relationship('Customers', back_populates='employee')

    def __repr__(self):
        return f"""
        EmployeeID: {self.employee_id}
        EmployeeFirstName: {self.first_name} 
        EmployeeLastName: {self.last_name} 
        EmployeeEmail: {self.email} 
        EmployeePhone: {self.phone}
        """


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    quantity_ordered = Column(Integer)
    price_each = Column(DECIMAL(10, 2))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    shipped_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    product = relationship('Products', back_populates='orders')
    customers_customers_id = Column(Integer, ForeignKey('customers.customers_id'), primary_key=True)
    customer = relationship('Customers', back_populates='order')

    def __repr__(self):
        return f"""
               OrdersID: {self.order_id}
               quantityOrdered: {self.quantity_ordered}
               PriceEach: {self.price_each}
               OrderDate: {self.order_date} 
               ShippedDate: {self.shipped_date} 
               Created_at: {self.created_at}
               ProductId: {self.products_product_id}
               {self.customer}
               """


class Resellers(Base):
    __tablename__ = 'resellers'

    reseller_id = Column(Integer, primary_key=True, autoincrement=True)
    reseller_name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    contact_name = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    manufacturer_manufacturer_id = Column(Integer, ForeignKey('manufacturer.manufacturer_id'), primary_key=True)
    manufacturer = relationship('Manufacturer', back_populates='resellers')
    products = relationship('Products', back_populates='resellers')

    def __repr__(self):
        return f"""
            ResellerID: {self.reseller_id}
            ResellerName: {self.reseller_name}
            ResellerAddress: {self.address}
            ResellerContactPerson: {self.contact_name}
            ResellerPhone: {self.phone} 
            ResellerEmail: {self.email}
            Products: {self.products}
            """


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    contact_name = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    zip_code = Column(String(100), nullable=False)
    resellers = relationship('Resellers', back_populates='manufacturer')

    def __repr__(self):
        return f"""
               ******************
               ManufacturingInfo:
               ******************
               ManufacturingID: {self. manufacturer_id}
               {self.manufacturer_name} {self.address}
               {self.contact_name} {self.phone} 
               {self.email} {self.city}
               {self.country} {self.zip_code}
               resellers: {self.resellers}
               """
=======
from mongoengine import EmailField, DecimalField, Document
from mongoengine import StringField, IntField, DateTimeField


class Customers(Document):
    email = EmailField(equired=True, unique=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    phone = StringField(required=True, unique=True)
    address = StringField(max_length=50, required=True)
    postal_code = StringField(max_length=20, required=True)
    city = StringField(max_length=50, required=True)
    country = StringField(max_length=50, required=True)

    def __init__(self, email, first_name, last_name, phone, address,
                 postal_code, city, country, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    meta = {'collection': 'customers'}


class Products(Document):
    prod_name = StringField(max_length=50, required=True)
    prod_number = StringField(max_length=50, required=True)
    prod_vendor = StringField(max_length=50, required=True)
    quantityin_stock = IntField(required=True)
    buy_price = DecimalField(precision=2)
    description = StringField(max_length=200)

    def __init__(self, prod_name, prod_number, prod_vendor, quantityin_stock, buy_price,
                 description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prod_name = prod_name
        self.prod_number = prod_number
        self.prod_vendor = prod_vendor
        self.quantityin_stock = quantityin_stock
        self.buy_price = buy_price
        self.description = description

    meta = {'collection': 'products'}


class Orders(Document):
    quantity_ordered = IntField(max_length=50, required=True)
    order_date = DateTimeField(required=True)
    price_each = DecimalField(precision=2)
    shipped_date = DateTimeField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    def __init__(self, quantity_ordered, order_date, price_each, shipped_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity_ordered = quantity_ordered
        self.order_date = order_date
        self.price_each = price_each
        self.shipped_date = shipped_date

    meta = {'collection': 'orders'}


class Cars(Document):
    register_number = StringField(max_length=7, required=True)
    brand = StringField(max_length=50, required=True)
    model = StringField(max_length=50, required=True)
    color = StringField(max_length=50, required=True)
    year = DateTimeField(max_length=50, required=True)

    def __init__(self, register_number, brand, model, color, year, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_number = register_number
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    meta = {'collection': 'cars'}


class Employees(Document):
    email = EmailField(max_length=50, required=True, unique=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, unique=True, required=True)
    address = StringField(max_length=50, required=True)
    city = StringField(max_length=50, required=True)
    postal_code = StringField(max_length=20, required=True)
    country = StringField(max_length=50, required=True)

    def __init__(self, email, first_name, last_name, phone, address, city,
                 postal_code, country, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country

    meta = {'collection': 'employees'}


class Offices(Document):
    office_name = StringField(max_length=50, required=True)
    address = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, required=True, unique=True)
    employee_fullname = StringField(max_length=50, required=True)
    employee_phone = StringField(max_length=50, required=True, unique=True)
    employee_email = EmailField(max_length=50, required=True, unique=True)

    def __init__(self, office_name, address, phone, employee_fullname, employee_phone,
                 employee_email,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.office_name = office_name
        self.address = address
        self.phone = phone
        self.employee_fullname = employee_fullname
        self.employee_phone = employee_phone
        self.employee_email = employee_email

    meta = {'collection': 'offices'}


class Suppliers(Document):
    email = EmailField(required=True, max_length=50, unique=True)
    name = StringField(required=True, max_length=50)
    phone = StringField(required=True, unique=True, max_length=50)
    address = StringField(required=True, max_length=50)
    city = StringField(max_length=50, required=True)
    postal_code = StringField(max_length=20, required=True)
    country = StringField(max_length=50, required=True)

    def __init__(self, email, name, phone, address,
                 postal_code, city, country, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.name = name
        self.phone = phone
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country

    meta = {'collection': 'suppliers'}


class Manufacturers(Document):
    email = EmailField(max_length=50, required=True, unique=True)
    name = StringField(max_length=50, required=True)
    phone = StringField(max_length=50, unique=True, required=True)
    contact_fullname = StringField(max_length=50, required=True)
    address = StringField(max_length=50, required=True)
    city = StringField(max_length=50, required=True)
    postal_code = StringField(max_length=20)
    country = StringField(max_length=50, required=True)

    def __init__(self, email, name, address, contact_fullname, phone,
                 city, postal_code, country, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.name = name
        self.contact_fullname = contact_fullname
        self.address = address
        self.phone = phone
        self.city = city
        self.postal_code = postal_code
        self.country = country

    meta = {'collection': 'manufacturers'}
>>>>>>> main
