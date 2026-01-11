from flask import Flask
from database import config
from flask_sqlalchemy import SQLAlchemy
from database.db import db


# instance from Flask
app=Flask(__name__)

# config SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


SQLAlchemy(app)





@app.route('/')
def home():
    return "welcome to flask"


# init DB
db.init_app(app)
with app.app_context():
    db.create_all()

# to run locally
if __name__=="__main__":
    app.run()

