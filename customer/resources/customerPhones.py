from flask_restful import Resource, reqparse
from datetime import datetime
from customer.models.customerPhones import CustomerPhones


class CustomerPhonesApi(Resource):

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('customerid', type=int, required=True, help="This field cannot be left blank!")
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('ccode', type=str, required=True)
        parser.add_argument('phoneno', type=str, required=True)

        try:
            payload = parser.parse_args()

            return CustomerPhones.updatephone(payload)

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500
