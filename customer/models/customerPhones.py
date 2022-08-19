from datetime import datetime
from customer.db import db


class CustomerPhones(db.Model):

    __tablename__ = 'CustomerPhones'

    def __init__(self, customerid, ccode, phoneno, phonetype, createdby=None, updatedby=None):
        self.CustomerId = customerid
        self.CountryCode = ccode
        self.PhoneNumber = phoneno
        self.PhoneType = phonetype
        self.CreatedBy = createdby
        self.UpdatedBy = updatedby

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
        for p in cls.query.filter_by(CustomerId=customerid).all():
            phones.append({'type': p.PhoneType, 'ccode': p.CountryCode, 'phone': p.PhoneNumber})
        return phones

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



