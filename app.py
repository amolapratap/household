# #starting of the app
# from flask import Flask
# from backend.models import db
# from flask_migrate import Migrate

# app=None


# def setup_app():
#     app=Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///household.sqlite3"  #having db file
#     migrate = Migrate(app, db) #migrate is used to add new attribue in tables in db
#     db.init_app(app)  #Flask app connected to db(SQL alchemy)
#     app.app_context().push() #Direct access to other modules
#     app.debug=True
#     print("Household serice app is stared...")
#     return app

# #call the setup_app
# setup_app()

# from backend.controllers import *

# if __name__=="__main__":
#     app.run()
    
    
    
# #this today


from flask import Flask
from backend.models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///household.sqlite3"
    app.debug = True

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register routes here safely
    with app.app_context():
        from backend.controllers import *

    return app

# This variable must exist for Vercel to find it
app = create_app()

if __name__ == "__main__":
    app.run()
