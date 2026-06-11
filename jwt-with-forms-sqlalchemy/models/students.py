from extensions import db

class Student(db.Model):
    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(
        db.Integer,
        nullable=False
    )

    student_class = db.Column(
        db.String(50),
        nullable=False
    )
       
        