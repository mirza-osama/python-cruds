from flask import request, jsonify, Blueprint
import bcrypt
from models.user import User
from extensions import db

from flask_jwt_extended import create_access_token


auth_bp = Blueprint("users", (__name__))

@auth_bp.route('/register', methods = ["POST"])

def regiter():
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    
    if not username:
        return jsonify({
            "message" : "username required"
        })
    if not password:
        return jsonify({
            "error" : "password required"
        })
    
    exist = User.query.filter_by(
        username = username
    ).first()
    
    if exist:
        return jsonify({
            "error" : "User exist"
        })
    
    hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    
    user = User(
        username = username,
        password = hash.decode()
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        "message" : "User registered"
    }),201
    
@auth_bp.route('/login', methods = ["POST"])

def login():
    
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    
    check_user = User.query.filter_by(
        username = username
    ).first()
    
    if not check_user:
        return jsonify({
            "message" : "user not found"
        })
        
    check_pass = bcrypt.checkpw(
        password.encode(),
        check_user.password.encode()
    )
    if not check_pass:
        return jsonify({
            "message" :"Password Wrong"
        })
        
    token = create_access_token(
        identity=str(check_user.id)
    )
    return jsonify({
        "message" : "login Succesfull",
        "token" : token
    })