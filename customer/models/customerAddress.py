from datetime import datetime
from customer.db import db


class CustomerAddress(db.Model):

    __tablename__ = 'CustomerAddress'

    def __init__(self, customerid, addresstype, address1, scode, pcode, ccode, address2=None, createdby=None, updatedby=None):
        self.CustomerId = customerid
        self.AddressType = addresstype
        self.Address1 = address1
        self.Address2 = address2
        self.StateCode = scode
        self.PostalCode = pcode
        self.CountryCode = ccode
        self.CreatedBy = createdby
        self.UpdatedBy = updatedby

    AddressId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerId = db.Column(db.Integer)
    AddressType = db.Column(db.String(100))
    Address1 = db.Column(db.String(100))
    Address2 = db.Column(db.String(100))
    StateCode = db.Column(db.String(3))
    PostalCode = db.Column(db.String(10))
    CountryCode = db.Column(db.String(3))
    StartEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    EndEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.strptime('9999-12-31 00:00:00', '%Y-%m-%d %H:%M:%S'))
    CreatedDate = db.Column(db.DateTime, default=datetime.now)
    CreatedBy = db.Column(db.String(45))
    UpdatedDate = db.Column(db.DateTime, default=datetime.now)
    UpdatedBy = db.Column(db.String(45))

    def json(self):
        return {'customerId': self.Customerid,
                'addressType': self.AddressType}

    @classmethod
    def find_by_customerid(cls, customerid):
        address = []
        for a in cls.query.filter_by(CustomerId=customerid).all():
            address.append({'type': a.AddressType, 'address1': a.Address1, 'address2': a.Address2, 'countyCode': a.CountryCode, 'postalCode': a.PostalCode, 'stateCode': a.StateCode})
        return address

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



