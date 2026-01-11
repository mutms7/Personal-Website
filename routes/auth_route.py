

from flask import Blueprint,request
from models.user import UserModel
from database.db import db


auth_router = Blueprint('auth', __name__, url_prefix='/auth')


@auth_router.route('/register', methods=['POST'])
def create_user():
        data=request.get_json()
        email=data['email']
        password=data['password']
        role=data['role']

        try:
            new_user=UserModel(email=email, password=password, role=role)
            db.session.add(new_user)
            db.session.commit()
        except:
            return "error"



