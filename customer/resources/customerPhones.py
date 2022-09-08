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
            _customerphones= CustomerPhones.find_by_customerptype(payload['customerid'], payload['type'])

            if _customerphones.PhoneType == payload['type'] and _customerphones.PhoneNumber == payload['phoneno']:
                return {'messageType': 'Success', "message": "customer with same phone number already exists."}
            elif _customerphones.PhoneType == payload['type'] and _customerphones.PhoneNumber != payload['phoneno']:

                _customerphones.EndEffectiveDate = datetime.now()
                _customerphones.UpdatedDate = datetime.now()
                _customerphones.UpdatedBy = CustomerPhonesApi.__name__
                _customerphones.save_to_db()
                new_phone = CustomerPhones(customerid=payload['customerid'],
                                           phonetype=payload['type'],
                                           ccode=payload['ccode'],
                                           phoneno=payload['phoneno'],
                                           createdby=CustomerPhonesApi.__name__,
                                           updatedby=CustomerPhonesApi.__name__)
                new_phone.save_to_db()
                return {'messageType': 'Success', "message": "customer phone number is updated successfully."}
            else:
                new_phone = CustomerPhones(customerid=payload['customerid'],
                                           phonetype=payload['type'],
                                           ccode=payload['ccode'],
                                           phoneno=payload['phoneno'],
                                           createdby=CustomerPhonesApi.__name__,
                                           updatedby=CustomerPhonesApi.__name__)
                new_phone.save_to_db()
                return {'messageType': 'Success', "message": "customer phone number is updated successfully."}, 201
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500
