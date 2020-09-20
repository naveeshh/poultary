from flask import request,Blueprint
from src.models.poultry import Orders
from src.setup import db

orders = Blueprint('orders', __name__, url_prefix='/orders')


@orders.route('/createorder', methods=['GET'])
def createorder():
    # a = request.get_json()
    # print(type(a))
    # x = Orders(order_id=a.get("order_id"), customer_id=a.get("customer_id"))
    # db.session.add(x)
    # db.session.commit()
    # return "successfully created {}".format(x.customer_id)
    return "lolo"

@orders.route('/deleteorder/<int:order_id>',methods=['DELETE'])
def delete_order(order_id):
    Orders.query.filter(Orders.order_id == order_id).delete()
    db.session.commit()
    return '', 204