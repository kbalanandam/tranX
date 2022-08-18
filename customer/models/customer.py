from datetime import datetime
from customer.db import db
from customer.models.customerEmails import CustomerEmails

class Customer(db.Model):

    __tablename__ = 'customer'

    def __init__(self, firstname, lastname, gender, customertype, middlename=None, dob=None, createdby=None, updatedby=None):
        self.FirstName = firstname
        self.MiddleName = middlename
        self.LastName = lastname
        self.Gender = gender
        self.DateOfBirth = dob
        self.CustomerTypeId = customertype
        self.CreatedBy = createdby
        self.UpdatedBy = updatedby

    customerId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(45))
    MiddleName = db.Column(db.String(45), nullable=True)
    LastName = db.Column(db.String(45))
    Gender = db.Column(db.String(1))
    DateOfBirth = db.Column(db.Date, nullable=True)
    CustomerBalance = db.Column(db.Float, nullable=True, default=0.00)
    StartEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    EndEffectiveDate = db.Column(db.DateTime, nullable=False, default=datetime.strptime('9999-12-31 00:00:00', '%Y-%m-%d %H:%M:%S'))
    CustomerTypeId = db.Column(db.Integer, nullable=False)
    AccountStatus = db.Column(db.Integer, nullable=False)
    StatusDateTime = db.Column(db.DateTime, default=datetime.now)
    CreatedDate = db.Column(db.DateTime, default=datetime.now)
    CreatedBy = db.Column(db.String(45))
    UpdatedDate = db.Column(db.DateTime, default=datetime.now)
    UpdatedBy = db.Column(db.String(45))

    def json(self):

        _customerid = self.customerId
        _email = CustomerEmails.find_by_id(_customerid)

        return {'CustomerId': self.customerId,
                'firstName': self.FirstName,
                'lastName': self.LastName,
                'accountBalance': self.CustomerBalance,
                'createdOn': str(self.StartEffectiveDate),
                'email': _email.Email}

    @classmethod
    def find_by_id(cls, customerid):
        return cls.query.filter_by(customerId=customerid).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



