#App routes
from flask import Flask,render_template,request,url_for,redirect
from flask import current_app as app
from .models import *
from datetime import date


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
            return redirect(url_for("admin_dashboard",name=uname))
        
        #professional dashboard  
        usr=Professional.query.filter_by(email=uname,password=pwd).first()
        if usr:    #if user exists
            return redirect(url_for("professional_dashboard",name=uname)) 
      
        #customer dashboard
        usr=Customer.query.filter_by(email=uname,password=pwd).first()
        if usr:    #if user exists
            return redirect(url_for("customer_dashboard",name=uname))
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


#common route for admin dashboard
@app.route("/admin/<name>")
def admin_dashboard(name):
    services=get_services()
    professionals=get_professionals()
    return render_template("admin_dashboard.html",name=name,services=services,professionals=professionals)

#common route for professional dashboard
@app.route("/professional/<name>")
def professional_dashboard(name):
    return render_template("professional_dashboard.html",name=name)

#common route for customer dashboard
@app.route("/customer/<name>")
def customer_dashboard(name):
    services=get_services()
    return render_template("customer_dashboard.html",name=name,services=services)




#may controller/routers
@app.route("/add_service/<name>",methods=["GET","POST"])
def add_service(name):
    if request.method=="POST":
        service_name=request.form.get("service_name")
        price=request.form.get("price")
        #time_required=request.form.get("time_required")
        description=request.form.get("description")
        
        # Creating a new Service object with the form data
        new_service=Service(name=service_name,price=price,description=description)
        # Add to the session and commit to save in database
        db.session.add(new_service)
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
           
    return render_template("add_service.html",name=name)


@app.route("/search/<name>",methods=["GET","POST"])
def search(name):
    if request.method=="POST":
        search_txt=request.form.get("search_txt")
        by_service=search_by_service(search_txt)
        by_professional=search_by_professional(search_txt)
        by_customer=search_by_customer(search_txt)
        #by_service_request=search_by_service_request(search_txt)
        if by_service:
            return render_template("admin_search_view.html",name=name,services=by_service)
        elif by_professional:
            return render_template("admin_search_view.html",name=name,professionals=by_professional)
        elif by_customer:
            return render_template("admin_search_view.html",name=name,customers=by_customer)
       # elif by_service_request:
       #     return render_template("admin_search_view.html",name=name,servicerequests=by_service_request)
        else:
            return render_template("admin_search_view.html",name=name,msg="Not Found")
    return redirect(url_for("admin_dashboard",name=name))     



@app.route("/edit_service/<id>/<name>",methods=["GET","POST"])
def edit_service(id,name):
    service=get_service(id)
    if request.method=="POST":
        #taking  data from form
        service_name=request.form.get("service_name")
        price=request.form.get("price")
        description=request.form.get("description")
        #updating data
        service.name=service_name
        service.price=price
        service.description=description
        db.session.commit()
        return redirect(url_for("admin_dashboard",name=name))
    
    return render_template("edit_service.html",name=name,service=service)
        

@app.route("/delete_service/<id>/<name>",methods=["GET","POST"])
def delete_service(id,name):
    service=get_service(id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("admin_dashboard",name=name))
    
    
#other supported function
def get_services():
    services = Service.query.all()  
    return services


def get_professionals():
    professionals = Professional.query.all()  
    return professionals
    
    
def search_by_service(search_txt):
    services = Service.query.filter(Service.name.ilike('%' + search_txt + '%')).all()
    return services


def search_by_professional(search_txt):
    professionals = Professional.query.filter(Professional.full_name.ilike('%' + search_txt + '%')).all()
    return professionals


def search_by_customer(search_txt):
    customers = Customer.query.filter(Customer.full_name.ilike('%' + search_txt + '%')).all()
    return customers

def search_by_service_request(search_txt):
    service_requests = Service_Request.query.filter(Service_Request.status.ilike('%' + search_txt + '%')).all()
    return service_requests       

def get_service(id):
    service = Service.query.filter_by(id=id).first()
    return service


                                                 