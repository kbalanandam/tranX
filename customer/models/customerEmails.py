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
    def find_by_customerid(cls, customerid):
        email = []
        for e in cls.query.filter(CustomerEmails.CustomerId == customerid,
                                  CustomerEmails.EndEffectiveDate > datetime.now()).all():
            email.append({'primary': e.IsPrimary, 'emailid': e.Email})
        if len(email) == 0:
            return None
        else:
            return email

    @classmethod
    def updateemail(cls, payload):

        try:
            exists = (cls.query.filter(CustomerEmails.CustomerId == payload['customerid'],
                                       CustomerEmails.Email == payload['email'],
                                       CustomerEmails.EndEffectiveDate > datetime.now()).first())

            if exists is not None:
                return {'messageType': 'Success', "message": "customer with same email already exists."}
            else:

                for _customeremail in cls.query.filter(CustomerEmails.CustomerId == payload['customerid'],
                                                       CustomerEmails.Email != payload['email'],
                                                       CustomerEmails.EndEffectiveDate > datetime.now()).all():
                    _customeremail.EndEffectiveDate = datetime.now()
                    _customeremail.UpdatedDate = datetime.now()
                    _customeremail.UpdatedBy = CustomerEmails.__module__
                    _customeremail.save_to_db()

                new_email = CustomerEmails(customerid=payload['customerid'],
                                       email=payload['email'],
                                       createdby=CustomerEmails.__module__,
                                       updatedby=CustomerEmails.__module__)
                new_email.save_to_db()

                return {'messageType': 'Success', "message": "customer email is updated successfully."}, 201

        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

