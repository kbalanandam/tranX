from datetime import datetime
from customer.db import db


class CustomerEmails(db.Model):

    __tablename__ = 'CustomerEmails'

    def __init__(self, customerid, email, isprimary=None,  createdby=None, updatedby=None):
        self.CustomerId = customerid
        self.Email = email
        self.IsPrimary = isprimary
        self.CreatedBy = createdby
        self.UpdatedBy = updatedby

    EmailId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerId = db.Column(db.Integer)
    Email = db.Column(db.String(100))
    IsPrimary = db.Column(db.String(1), nullable=True, default='Y')
    StartEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    EndEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.strptime('9999-12-31 00:00:00', '%Y-%m-%d %H:%M:%S'))
    CreatedDate = db.Column(db.DateTime, default=datetime.now)
    CreatedBy = db.Column(db.String(45))
    UpdatedDate = db.Column(db.DateTime, default=datetime.now)
    UpdatedBy = db.Column(db.String(45))

    def json(self):
        return {'CustomerId': self.customerid,
                'email': self.Email}

    @classmethod
    def find_by_id(cls, customerid):
        return cls.query.filter_by(CustomerId=customerid).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



