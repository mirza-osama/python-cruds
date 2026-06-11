from flask import Blueprint
from flask import request
from flask import jsonify

from extensions import db

from models.students import Student

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

student_bp = Blueprint(
    "students",
    (__name__)
)

@student_bp.route(
    "/students",
    methods=["POST"]
)
@jwt_required()

def create_student():

    current_user = get_jwt_identity()

    data = request.json

    student = Student(
        name=data.get('name'),
        course=data.get('course')
    )

    db.session.add(student)

    db.session.commit()

    return jsonify({
        "message":"Student Added",
        "logged_user":current_user
    })
    
@student_bp.route(
    "/students",
    methods=["GET"]
)
@jwt_required()

def get_students():

    students = Student.query.all()

    result = []

    for student in students:

        result.append(
            student.to_dict()
        )

    return jsonify(result)

@student_bp.route(
    "/students/<int:id>",
    methods=["GET"]
)
@jwt_required()

def get_student(id):

    student = Student.query.get(id)

    if not student:

        return jsonify({
            "error":"Not Found"
        }),404

    return jsonify(
        student.to_dict()
    )
    
@student_bp.route(
    "/students/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def update_student(id):

    student = Student.query.get(id)

    if not student:

        return jsonify({
            "error":"Not Found"
        }),404

    data = request.json

    student.name = data["name"]

    student.course = data["course"]

    db.session.commit()

    return jsonify({
        "message":"Updated"
    })
    
@student_bp.route(
    "/students/<int:id>",
    methods=["DELETE"]
)   
@jwt_required()
def delete_student(id):

    student = Student.query.get(id)

    if not student:

        return jsonify({
            "error":"Not Found"
        }),404

    db.session.delete(student)

    db.session.commit()

    return jsonify({
        "message":"Deleted"
    })