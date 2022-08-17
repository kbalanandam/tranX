from flask import Flask
from flask_restful import Api
from db import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tranX'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()
