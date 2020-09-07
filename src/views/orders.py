from src.setup import app,db
from flask import request
from src.models.poultry import Orders






@app.route('/createorder', methods=['POST'])
def createorder():
    a = request.get_json()
    print(type(a))
    x = Orders(order_id=a.get("order_id"), customer_id=a.get("customer_id"))
    db.session.add(x)
    db.session.commit()
    return "successfully created {}".format(x.customer_id)


@app.route('/deleteorder/<int:order_id>',methods=['DELETE'])
def delete_user(order_id):
    Orders.query.filter(Orders.order_id == order_id).delete()
    db.session.commit()
    return '', 204