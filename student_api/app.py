from flask import Flask
from Config import Config
from database import db
from routes import student_bp

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(student_bp)

with app.app_context():
    db.create_all()            # XAMPP DB mein table automatically ban jayegi

if __name__ == "__main__":
    app.run(debug=True)