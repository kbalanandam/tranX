from flask_restful import Resource, reqparse
from datetime import datetime
from customer.models.customerPhones import CustomerPhones
from customer.models.customer import Customer


class CustomerPhonesApi(Resource):

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('customerid', type=int, required=True, help="This field cannot be left blank!")
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('ccode', type=str, required=True)
        parser.add_argument('phoneno', type=str, required=True)

        try:
            payload = parser.parse_args()

            _customer = Customer.find_by_id(payload['customerid'])
            if _customer is not None:

                return CustomerPhones.updatephone(payload)
            else:
                return {'messageType': 'Warning', 'message': 'customer not exists.'}, 404

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500
