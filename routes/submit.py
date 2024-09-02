from flask import Blueprint, jsonify, request, session

from models import Question, Submit, db
from utility import authentication_required
submit_bp = Blueprint('submit', __name__)

@submit_bp.route('/submit', methods=['POST'])
def submit_answer():
    group = authentication_required(session)
    data = request.json
    group_id = group.id
    question_id = data['question_id']
    submitted_answer = data['answer']

    question = Question.query.get(question_id)
    if not question:
        return jsonify({"error": "Invalid question ID"}), 404

    is_correct = (submitted_answer == question.answer)
    
    new_submit = Submit(
        group_id=group_id,
        question_id=question_id,
        answer=submitted_answer,
        result=is_correct
    )
    db.session.add(new_submit)
    
    question.total_submits += 1
    if is_correct:
        question.correct_submits += 1
    
    db.session.commit()
    
    return jsonify({"result": is_correct})