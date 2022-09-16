from flask_restful import Resource, reqparse, request
from customer.models.customer import Customer
from customer.models.customerPhones import CustomerPhones
from customer.models.customerEmails import CustomerEmails
from customer.models.customerAddress import CustomerAddress


class CustomerApi(Resource):

    def get(self, customerid):
        try:
            _customer = Customer.find_by_id(customerid)
            if _customer is not None:
                return _customer.json()
            else:
                return {'messageType': 'Warning', 'message': 'customer: {} not exists.'.format(customerid)}, 404

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500

    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument('fname', type=str, required=True, help="This field cannot be left blank!")
        parser.add_argument('mname', type=str, required=False)
        parser.add_argument('lname', type=str, required=True, help="This field cannot be left blank!")
        parser.add_argument('gender', type=str, required=True, help="This field cannot be left blank!")
        parser.add_argument('dob', type=str, required=False)
        parser.add_argument('customertype', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('address', type=str, required=True)

        try:
            phones = []
            payload = request.json
            if payload['phone']:
                for phone in payload['phone']:
                    phones.append(phone)

            address = []
            if payload['address']:
                for adr in payload['address']:
                    address.append(adr)

            _customer = parser.parse_args()
            new = Customer(firstname=_customer['fname'], middlename=_customer['mname'], lastname=_customer['lname'], gender=_customer['gender'],
                           customertype=_customer['customertype'], createdby=CustomerApi.__name__,
                           updatedby=CustomerApi.__name__)
            new.save_to_db()
            new_email = CustomerEmails(customerid=new.customerId, email=_customer['email'], createdby=CustomerApi.__name__,
                           updatedby=CustomerApi.__name__)
            new_email.save_to_db()
            for i in phones:
                new_phone = CustomerPhones(customerid=new.customerId, phonetype=i['type'], ccode=i['ccode'], phoneno=i['phoneno'], createdby=CustomerApi.__name__,
                           updatedby=CustomerApi.__name__)

                new_phone.save_to_db()

            for a in address:
                new_address = CustomerAddress(customerid=new.customerId, addresstype=a['type'], address1=a['address1'], address2=a['address2'], ccode=a['countrycode'], scode=a['statecode'], pcode=a['postalcode'],createdby=CustomerApi.__name__,
                           updatedby=CustomerApi.__name__)

                new_address.save_to_db()

            return {'messageType': 'Success', "message": "customer id: {}, is created successfully.".format(new.customerId)}
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500



