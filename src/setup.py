from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Naveesh/Downloads/dbdatatest.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerty123@localhost:5432/poultry"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

db.create_all()
