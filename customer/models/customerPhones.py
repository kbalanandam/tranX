from datetime import datetime
from customer.db import db


class PhonesModel(db.Model):

    __tablename__ = 'customerPhones'

    def __init__(self, customerid, ccode, phoneno, isprimary, startdate):
        self.customerid = customerid
        self.countrycode = ccode
        self.phonenumber = phoneno
        self.isprimary = isprimary
        self.startdate = startdate

    PhoneId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerId = db.Column(db.Integer)
    CountryCode = db.Column(db.String(5))
    PhoneNumber = db.Column(db.String(20))
    IsPrimary = db.Column(db.String(1))
    EffectiveStartDate = db.Column(db.DateTime, nullable=False)
    EffectiveEndDate = db.Column(db.DateTime, nullable=False, default='9999-12-31 00:00:00')
    CreatedDate = db.Column(db.DateTime, default=datetime.utcnow)
    CreatedBy = db.Column(db.String(45))
    UpdatedDate = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedBy = db.Column(db.String(45))



