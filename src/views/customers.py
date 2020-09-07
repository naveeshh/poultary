from src.setup import app,db
from flask import request
from src.models.poultry import Customers





@app.route('/createuser', methods=['POST'])
def createuser():
    a = request.get_json()
    print(type(a))
    x = Customers(customer_name=a.get("customer_name"), customer_adress=a.get("customer_adress"),work_aera=a.get("work_adress"))
    db.session.add(x)
    db.session.commit()
    return "successfully created {}".format(x.customer_id)


@app.route('/updateuser')
def profile():
    return "successfully added"


@app.route('/deleteuser/<int:customer_id>',methods=['DELETE'])
def delete_user(customer_id):
    Customers.query.filter(Customers.customer_id == customer_id).delete()
    db.session.commit()
    return '', 204

# def delete():
#     Customer.query.filter_by(customer_id=9).delete()
#     db.session.commit()
#     return "successfully deleted"

@app.route('/')
def index():
    # x = Customer(customer_name='dad1', customer_adress='miltary', work_aera='miltary2')
    # db.session.add(x)
    # db.session.commit()
    # a = Customer.query.all()
    # for i in a:
    #     print(i)
    #     print(type(i))
    #     print(i.customer_name)
    return 'index'

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return "post meathos"
    else:
        return "retuen get meathod"

