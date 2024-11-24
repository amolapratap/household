#Data models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy








db=SQLAlchemy()


#Entity1 Professional
class Professional(db.Model):
    __tablename__="professional"
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    #role=db.Column(db.integer,nullable=False)
    full_name=db.Column(db.String,nullable=False)
    service_type=db.Column(db.String,nullable=False)              #dropdown from available service
    experience=db.Column(db.Integer,nullable=False)
    address=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    date_created=db.Column(db.String,default=0)
    mobile_number=db.Column(db.Integer,nullable=False)
    description=db.Column(db.String)
    rating=db.Column(db.String,default=0)
    rating_count=db.Column(db.String,default=0)
    password=db.Column(db.String,nullable=False)
    
    
    
    
    
#Entity2 Customer
class Customer(db.Model):
    __tablename__="customer"
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    #role=db.Column(db.integer,nullable=False)
    full_name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    mobile_number=db.Column(db.Integer,nullable=False)
    date_created=db.Column(db.String)
    description=db.Column(db.String)
    password=db.Column(db.String,nullable=False)  
    
    
    
#Entity3 Service
class Service(db.Model):
    __tablename__="service"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,default=0.0)
    action=db.Column(db.String,default="Edit/Delte")
    description=db.Column(db.String)    
    
    
    
#Entity4 Service Request
class Service_Request(db.Model):
    __tablename__="servicerequest"
    id = db.Column(db.Integer, primary_key=True)
    Service_id = db.Column(db.Integer, db.ForeignKey("service.id"),nullable=False)
    Customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"),nullable=False)
    Professional_id = db.Column(db.Integer, db.ForeignKey("professional.id"),nullable=False)
    date_of_request=db.Column(db.String)
    service_date=db.Column(db.String)
    date_of_completion=db.Column(db.String)
    description=db.Column(db.String)  
    status=db.Column(db.String,default=0) 
    rating=db.Column(db.String,default=0)  
    # Relationships
    #service_name = db.relationship('service', backref='servicerequests')  #Service_id can access his name
   
    service = db.relationship("Service", backref="Servicerequests")  # Access Service details
    customer = db.relationship("Customer", backref="servicerequests")  # Access Customer details
    professional = db.relationship("Professional", backref="servicerequests")  # Access Professional details
     