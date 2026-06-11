from flask import request, render_template, Blueprint, redirect, flash, make_response
from models.user import User
from extensions import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_jwt_extended import create_access_token

user_bp = Blueprint(
    "user",
    __name__
)

@user_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            username=username
        ).first()

        if user:

            flash("Username already exists")

            return redirect("/register")

        hashed_password = generate_password_hash(
            password
        )

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        flash("Register Successful")

        return redirect("/login")

    return render_template("register.html")
    
    
@user_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User.query.filter_by(
            username=username
        ).first()

        if not user:

            flash("User not found")

            return redirect("/login")

        if not check_password_hash(
            user.password,
            password
        ):

            flash("Wrong Password")

            return redirect("/login")

        token = create_access_token(
            identity=str(user.id)
        )

        response = make_response(
            redirect("/students")
        )

        response.set_cookie(
            "access_token",
            token,
            httponly=True
        )

        return response

    return render_template("login.html")

@user_bp.route("/logout")
def logout():

    response = make_response(
        redirect("/login")
    )

    response.delete_cookie(
        "access_token"
    )

    return response

    
    
    
    
    
    
    