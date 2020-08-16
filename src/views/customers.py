from src.setup import app,db
from flask import request
from src.models.poultry import Customer


@app.route('/user/<username>')
def profile(username):
    a = Customer.query.filter_by(customer_name=username).first()
    return {"customer_name": a.customer_name, "customer_adress":a.customer_adress}


@app.route('/createuser', methods=['POST'])
def createuser():
    a = request.get_json()
    print(type(a))
    x = Customer(customer_name=a.get("customer_name"), customer_adress=a.get("customer_adress"),work_aera=a.get("work_aera"))
    db.session.add(x)
    db.session.commit()
    return "successfully added {}".format(x.customer_id)

@app.route('/')
def index():
    x = Customer(customer_name='dad1', customer_adress='miltary', work_aera='miltary2')
    db.session.add(x)
    db.session.commit()
    a = Customer.query.all()
    for i in a:
        print(i)
        print(type(i))
        print(i.customer_name)
    return 'index'

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return "post meathos"
    else:
        return "retuen get meathod"

