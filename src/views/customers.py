from flask import request

# from src.models.poultry import Customers
from flask.views import MethodView
from src.handlers.handler_customer import addcustomer


class Customers(MethodView):
    def get(self):
        return "rupesh"

    def post (self):
        a = request.get_json()
        return addcustomer(a)


cust = Customers.as_view("navesh")




