import datetime

from sqlalchemy import DateTime

from service import db

# @as_declarative()
# class Base:
#     def _asdict(self):
#         return {c.key: getattr(self,c.key) for c in inspect(self).mapper.column_attrs}


class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), unique=True, nullable=False)
    customer_address = db.Column(db.String(120), unique=True, nullable=False)
    customer_ph_num = db.Column(db.Long, nullable=False)
    customer_details = db.Column(db.String(120), unique=True, nullable=True)
    work_area = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean(), default=False)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'),nullable=False)
    order_status= db.Column(db.String(120),nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean(), default=False)


class OrderDetails(db.Model):
    order_details_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'),nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    actual_price = db.Column(db.Float, nullable=False)
    discount =  db.Column(db.Float, nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean(), default=False)


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(120), unique=True, nullable=False)
    product_price =  db.Column(db.Integer, nullable=False)
    product_details =  db.Column(db.String(300), nullable=True)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean(), default=False)


class DailyProductPrice(db.Model):
    serial_no = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'),nullable=False)
    product_price =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean(), default=False)
