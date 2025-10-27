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

# Create Flask instance
app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///household.sqlite3"
app.debug = True

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)
app.app_context().push()

print("Household service app is started...")

# ✅ Import routes *after* the app is created and pushed to context
# This must be outside any function to avoid 'import * only allowed at module level'
from backend import controllers

# ✅ For Vercel, we export `app`
# Vercel looks for `app` (not running it manually)
if __name__ == "__main__":
    app.run()
