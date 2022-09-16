from datetime import date, datetime
from customer.db import db


class CustomerPhones(db.Model):

    __tablename__ = 'CustomerPhones'

    def __init__(self, customerid, ccode, phoneno, phonetype, enddate=None, createdby=None, updatedby=None):
        self.CustomerId = customerid
        self.CountryCode = ccode
        self.PhoneNumber = phoneno
        self.PhoneType = phonetype
        self.CreatedBy = createdby
        self.UpdatedBy = updatedby
        self.EndEffectiveDate = enddate

    PhoneId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerId = db.Column(db.Integer)
    CountryCode = db.Column(db.String(5))
    PhoneNumber = db.Column(db.String(20))
    PhoneType = db.Column(db.String(1))
    StartEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    EndEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.strptime('9999-12-31 00:00:00', '%Y-%m-%d %H:%M:%S'))
    CreatedDate = db.Column(db.DateTime, default=datetime.now)
    CreatedBy = db.Column(db.String(45))
    UpdatedDate = db.Column(db.DateTime, default=datetime.now)
    UpdatedBy = db.Column(db.String(45))

    def json(self):
        return {'CustomerId': self.CustomerId,
                'Country Code': self.CountryCode,
                'Phone': self.PhoneNumber}

    @classmethod
    def find_by_customerid(cls, customerid):
        phones = []
        for p in cls.query.filter(CustomerPhones.CustomerId == customerid, CustomerPhones.EndEffectiveDate > datetime.now()).all():
            phones.append({'type': p.PhoneType, 'ccode': p.CountryCode, 'phone': p.PhoneNumber})
        if len(phones) == 0:
            return None
        else:
            return phones

    @classmethod
    def updatephone(cls, payload):

        try:

            exists = (cls.query.filter(CustomerPhones.CustomerId == payload['customerid'],
                                CustomerPhones.PhoneNumber == payload['phoneno'],
                                CustomerPhones.PhoneType == payload['type'],
                                CustomerPhones.EndEffectiveDate > datetime.now()).first())
            if exists is not None:
                return {'messageType': 'Success', "message": "customer with same phone number already exists."}

            else:
                for _customerphones in cls.query.filter(CustomerPhones.CustomerId == payload['customerid'],
                                CustomerPhones.PhoneNumber != payload['phoneno'],
                                CustomerPhones.PhoneType == payload['type'],
                                CustomerPhones.EndEffectiveDate > datetime.now()).all():
                    _customerphones.EndEffectiveDate = datetime.now()
                    _customerphones.UpdatedDate = datetime.now()
                    _customerphones.UpdatedBy = CustomerPhones.__module__
                    _customerphones.save_to_db()

                new_phone = CustomerPhones(customerid=payload['customerid'],
                                           phonetype=payload['type'],
                                           ccode=payload['ccode'],
                                           phoneno=payload['phoneno'],
                                           createdby=CustomerPhones.__module__,
                                           updatedby=CustomerPhones.__module__)
                new_phone.save_to_db()
                return {'messageType': 'Success', "message": "customer phone number is updated successfully."}, 201
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()




