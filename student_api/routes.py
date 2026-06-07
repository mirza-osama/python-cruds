from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from database import db
from model import Student

student_bp = Blueprint('student', __name__)

# ── Web Form (browser ke liye) ──────────────────────────────
@student_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name  = request.form.get('name')
        email = request.form.get('email')
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('student.home'))
    return render_template('index.html')


# ── API Endpoints (Postman / curl ke liye) ──────────────────

# 1. Naya student add karo (POST)
@student_bp.route('/api/students', methods=['POST'])
def add_student():
    data  = request.get_json()
    name  = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name aur Email dono required hain'}), 400

    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student add ho gaya!', 'id': student.id}), 201


# 2. Saare students dekho (GET)
@student_bp.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    result = [{'id': s.id, 'name': s.name, 'email': s.email} for s in students]
    return jsonify(result), 200


# 3. Ek student dekho ID se (GET)
@student_bp.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student nahi mila'}), 404
    return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 200


# 4. Student update karo (PUT)
@student_bp.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student nahi mila'}), 404

    data = request.get_json()
    student.name  = data.get('name', student.name)
    student.email = data.get('email', student.email)
    db.session.commit()
    return jsonify({'message': 'Student update ho gaya!'}), 200


# 5. Student delete karo (DELETE)
@student_bp.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student nahi mila'}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student delete ho gaya!'}), 200