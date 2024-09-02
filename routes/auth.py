from flask import Blueprint, jsonify, request, session

# from group import Group
from models import Group, db
from utility import authentication_required, get_key_from_json_request

auth_bp = Blueprint('auth', __name__)

@auth_bp.get("/authenticated_hello")
def auth_hello():
    group = authentication_required(session)
    return "hiii " + group.group_name + "\n"

@auth_bp.post("/login")
def login():
    a = request.json
    group_name = get_key_from_json_request(a, "group_name")
    password = get_key_from_json_request(a, "password")
    gr = Group.query.filter_by(group_name=group_name, password=password).first()
    if gr == None:
        return "groupname or password is incorrect", 404

    session["group_id"] = gr.id 
    return jsonify(group_id=gr.id)

@auth_bp.post("/new-group")
def create_group():
    data = request.json
    new_group = Group(
        group_name=data['group_name'],
        password=data['password'],
        keys=int(data['keys'])
    )

    db.session.add(new_group)
    db.session.commit()
    group_id = Group.query.filter_by(group_name=data['group_name']).first().id
    return jsonify({"id": group_id})