from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect

from extensions import db

from models.students import Student

from flask_jwt_extended import (
    decode_token
)

from functools import wraps

students_bp = Blueprint(
    "students",
    __name__
)

def login_required(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        token = request.cookies.get(
            "access_token"
        )

        if not token:

            return redirect("/login")

        try:

            decode_token(token)

        except:

            return redirect("/login")

        return fn(*args, **kwargs)

    return wrapper

@students_bp.route("/students")
@login_required
def students():

    all_students = Student.query.all()

    return render_template(
        "students.html",
        students=all_students
    )


@students_bp.route(
    "/student/add",
    methods=["GET", "POST"]
)
@login_required
def add_student():

    if request.method == "POST":

        student = Student(
            name=request.form["name"],
            age=request.form["age"],
            student_class=request.form["student_class"]
        )

        db.session.add(student)

        db.session.commit()

        return redirect("/students")

    return render_template(
        "add_student.html"
    )


@students_bp.route(
    "/student/<int:id>"
)
@login_required
def show_student(id):

    student = Student.query.get_or_404(id)

    return render_template(
        "show_student.html",
        student=student
    )


@students_bp.route(
    "/student/edit/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.name = request.form["name"]

        student.age = request.form["age"]

        student.student_class = request.form["student_class"]

        db.session.commit()

        return redirect("/students")

    return render_template(
        "edit_student.html",
        student=student
    )


@students_bp.route(
    "/student/delete/<int:id>",
    methods=["POST"]
)
@login_required
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)

    db.session.commit()

    return redirect("/students")