import os
from flask import Flask, session, request, jsonify, make_response
from datetime import datetime as dt
from utility import *
# from group import Group
from models import db, Question, Submit
from routes.auth import auth_bp
from routes.question import question_bp
from routes.submit import submit_bp
from flask_cors import CORS
from datetime import timedelta



app = Flask(__name__)
CORS(app, origins=['*'], supports_credentials=True)
app.secret_key = b'yiwpq9853nbmc/sdkf,e.,vx%32985&&%$#@weh' # TODO: change this maybe
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "media"

app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # Lax or 'Strict'
app.config['SESSION_COOKIE_SECURE'] = True  # Enable if you're using HTTPS
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # Set session expiration
app.config['SESSION_PERMANENT'] = True  # Make session persistent

db.init_app(app)
app.register_blueprint(auth_bp, url_prefix='')
app.register_blueprint(question_bp, url_prefix='')
app.register_blueprint(submit_bp, url_prefix='')


@app.get("/hello")
def hello():
    return "hiii\n", 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host="0.0.0.0")