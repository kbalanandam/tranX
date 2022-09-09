from flask_restful import Resource, reqparse
from datetime import datetime
from customer.models.customerEmails import CustomerEmails


class CustomerEmailsApi(Resource):

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('customerid', type=int, required=True, help="This field cannot be left blank!")
        parser.add_argument('email', type=str, required=True)

        try:
            payload = parser.parse_args()
            _customeremail= CustomerEmails.find_by_customerid(payload['customerid'])

            if _customeremail.CustomerId == payload['customerid'] and _customeremail.Email == payload['email']:
                return {'messageType': 'Success', "message": "customer with same email already exists."}
            elif _customeremail.CustomerId == payload['customerid'] and _customeremail.Email != payload['email']:

                _customeremail.EndEffectiveDate = datetime.now()
                _customeremail.UpdatedDate = datetime.now()
                _customeremail.UpdatedBy = CustomerEmailsApi.__name__
                _customeremail.save_to_db()
                new_email = CustomerEmails(customerid=payload['customerid'],
                                           email=payload['email'],
                                           createdby=CustomerEmailsApi.__name__,
                                           updatedby=CustomerEmailsApi.__name__)
                new_email.save_to_db()
                return {'messageType': 'Success', "message": "customer email is updated successfully."}
            else:
                _customeremail.EndEffectiveDate = datetime.now()
                _customeremail.UpdatedDate = datetime.now()
                _customeremail.UpdatedBy = CustomerEmailsApi.__name__
                _customeremail.save_to_db()
                new_email = CustomerEmails(customerid=payload['customerid'],
                                           email=payload['email'],
                                           createdby=CustomerEmailsApi.__name__,
                                           updatedby=CustomerEmailsApi.__name__)
                new_email.save_to_db()
                return {'messageType': 'Success', "message": "customer email is updated successfully."}, 201
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500
