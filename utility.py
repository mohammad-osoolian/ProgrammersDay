from werkzeug.exceptions import BadRequest, Forbidden
from models import Group, db

def get_key_from_json_request(j, key):
    if key in j:
        return j[key]
    raise BadRequest(description="field "+key+" is missing")


def authentication_required(session) -> Group:
    if "group_id" not in session:
        raise Forbidden
    group_id = session["group_id"]
    gr = Group.query.filter_by(id=group_id).first()
    if gr == None:
        raise Forbidden
    return gr
