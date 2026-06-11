from flask import Flask

from config import config

from extensions import db, jwt

from routes.user import user_bp

from routes.students import students_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_super_secret_key"

app.config.from_object(config)

db.init_app(app)

jwt.init_app(app)

app.register_blueprint(user_bp)

app.register_blueprint(students_bp)

with app.app_context():

    db.create_all()


if __name__ == "__main__":

    app.run(debug=True)