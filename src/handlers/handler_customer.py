from src.setup import db
from src.models.poultry import Customers


def addcustomer(a):
    print(type(a))
    x = Customers(customer_name=a.get("customer_name"), customer_adress=a.get("customer_adress"),
                  work_aera=a.get("work_adress"))
    db.session.add(x)
    db.session.commit()
    return "successfully created {}".format(x.customer_id)
