import os
from flask import Blueprint, jsonify, request, current_app

from models import Question, db
question_bp = Blueprint('question', __name__)

@question_bp.route('/new-question', methods=['POST'])
def create_question():
    zip_file = request.files.get('zip_file')
    if zip_file:
        zip_file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], zip_file.filename)
        zip_file.save(zip_file_path)

    new_question = Question(
        id=int(request.form['id']),
        title=request.form['title'],
        text=request.form['text'],
        cost=int(request.form['cost']),
        score=int(request.form['score']),
        is_starred=request.form.get('is_starred', '0') == '1',
        zip_file_name=zip_file.filename,
        answer=request.form['answer']
    )

    db.session.add(new_question)
    db.session.commit()

    return jsonify({"message": "Question created successfully", "question_id": new_question.id})

