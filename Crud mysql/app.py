from flask import Flask
from database import get_connect

app = Flask(__name__)

@app.route('/')
def show():
    return ("Hellow world   ")
app.run(debug=True)