from flask import Flask

from config import config

from extensions import db
from extensions import jwt

from routes.user import auth_bp
from routes.students import student_bp

app = Flask(__name__)

app.config.from_object(
    config
)

db.init_app(app)

jwt.init_app(app)

app.register_blueprint(
    auth_bp
)

app.register_blueprint(
    student_bp
)

with app.app_context():

    db.create_all()

if __name__ == "__main__":

    app.run(debug=True)