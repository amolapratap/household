#App routes
from flask import Flask,render_template,request
from flask import current_app as app
from .models import *


@app.route("/")
def Home():
    return render_template("index.html")

 
@app.route("/login",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password")
        
        #admin dashboard
        if uname=="admin@gmail.com" and pwd=="adminpassword":
            return render_template("admin_dashboard.html")
        
        #professional dashboard  
        usr=Professional.query.filter_by(email=uname,password=pwd).first()
        if usr:    #if user exists
            return render_template("professional_dashboard.html",msg=uname)  
      
        #customer dashboard
        usr=Customer.query.filter_by(email=uname,password=pwd).first()
        if usr:    #if user exists
            return render_template("customer_dashboard.html",msg=uname)
        else: 
            return render_template("login.html",msg="Inavalid user and credetials")
        
    return render_template("login.html",msg="")


@app.route("/register_professional",methods=["GET","POST"])
def register_professional():
    if request.method=="POST":
        uname=request.form.get("user_name")
        if uname =="":
            return render_template("professional_signup.html",msg="you not entered email, please enter Email")
        else:
            ex_usr=Professional.query.filter_by(email=uname).first()
            if ex_usr:
                return render_template("professional_signup.html",msg="User already exists, please login")
        full_name=request.form.get("full_name")
        Service_type=request.form.get("service_type")
        experience=request.form.get("experience")
        address=request.form.get("address")
        pin_code=request.form.get("pin_code")
        description=request.form.get("description")
        pwd=request.form.get("password")
        
        # Creating a new Professional object with the form data
        new_usr=Professional(email=uname,full_name=full_name,service_type=Service_type,experience=experience,address=address,pincode=pin_code,description=description,password=pwd)
        # Add to the session and commit to save in database
        db.session.add(new_usr)
        db.session.commit()
        return render_template("login.html",msg="Registration Successfull, login now")
        
    return render_template("professional_signup.html",msg="")


@app.route("/register_customer",methods=["GET","POST"])
def register_customer():
    if request.method=="POST":
        uname=request.form.get("user_name")
        if uname =="":
            return render_template("customer_signup.html",msg="you not entered email, please enter Email")
        else:
            ex_usr=Customer.query.filter_by(email=uname).first()
            if ex_usr:
                return render_template("customer_signup.html",msg="User already exists, please login")
        full_name=request.form.get("full_name")
        address=request.form.get("address")
        pin_code=request.form.get("pin_code")
        description=request.form.get("description")
        pwd=request.form.get("password")
        
        # Creating a new Professional object with the form data
        new_usr=Customer(email=uname,full_name=full_name,address=address,pincode=pin_code,description=description,password=pwd)
        # Add to the session and commit to save in database
        db.session.add(new_usr)
        db.session.commit()
        return render_template("login.html",msg="Registration Successfull, login now")
        
    return render_template("customer_signup.html",msg="")