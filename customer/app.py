from flask import Flask
from flask_restful import Api
from db import db
from flask_cors import CORS
from customer.resources.customer import CustomerApi
from customer.resources.customerPhones import CustomerPhonesApi
from customer.resources.customerEmails import CustomerEmailsApi


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tranX'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
api = Api(app)
CORS(app)


api.add_resource(CustomerApi, '/api/customer/<int:customerid>', endpoint='customer')
api.add_resource(CustomerApi, '/api/customer', endpoint='createcustomer')
api.add_resource(CustomerPhonesApi, '/api/customer/phones', endpoint='udpdatephone')
api.add_resource(CustomerEmailsApi, '/api/customer/email', endpoint='udpdateemail')

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        app.run(port=5000, debug=True)



