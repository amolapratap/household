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
    description=db.Column(db.String)
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
    date_created=db.Column(db.String)
    description=db.Column(db.String)
    password=db.Column(db.String,nullable=False)  
    
    
    
#Entity3 Service
class Service(db.Model):
    __tablename__="service"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,default=0.0)
    time_required=db.Column(db.String)
    description=db.Column(db.String)    
    
    
    
#Entity4 Servie Request
class Servie_Request(db.Model):
    __tablename__="servierequest"
    id = db.Column(db.Integer, primary_key=True)
    Service_id = db.Column(db.Integer, db.ForeignKey("service.id"),nullable=False)
    Customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"),nullable=False)
    Professional_id = db.Column(db.Integer, db.ForeignKey("professional.id"),nullable=False)
    date_of_request=db.Column(db.String)
    date_of_completion=db.Column(db.String)
    description=db.Column(db.String)  
    status=db.Column(db.String,default=0) 
    rating=db.Column(db.String,default=0)  
     