from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.views.customers import cust

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Naveesh/Downloads/dbdatatest.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerty123@localhost:5432/poultry"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.add_url_rule("/user", methods=['GET','POST'], view_func=cust)

db = SQLAlchemy(app)

db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
