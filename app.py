import os
from flask import Flask, session, request, jsonify, make_response
from datetime import datetime as dt
from utility import *
# from group import Group
from models import db, Question, Submit
from routes.auth import auth_bp
from routes.question import question_bp
from routes.submit import submit_bp


app = Flask(__name__)
app.secret_key = b'yiwpq9853nbmc/sdkf,e.,vx%32985&&%$#@weh' # TODO: change this maybe
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "media"
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
    app.run(debug=True)