from service import db

# @as_declarative()
# class Base:
#     def _asdict(self):
#         return {c.key: getattr(self,c.key) for c in inspect(self).mapper.column_attrs}


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), unique=True, nullable=False)
    customer_adress = db.Column(db.String(120), unique=True, nullable=False)
    work_aera = db.Column(db.String(120), unique=True, nullable=False)
