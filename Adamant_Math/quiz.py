import random
from flask import render_template, request, session, redirect, url_for

def quiz():
    if 'equations' not in session or not session['equations']:
        return redirect(url_for('memory_bank'))
    if 'score' not in session:
        session['score'] = 0
    if 'questions_answered' not in session:
        session['questions_answered'] = 0
    
    equations = session['equations']
    asked_questions = session.get('asked_questions', [])
    available_questions = [eq for eq in equations if eq not in asked_questions]

    if not available_questions:
        return render_template("quiz.html", quiz_completed=True, score=session['score'])

    question = random.choice(available_questions)
    left_side = question.split('=')[0]

    asked_questions.append(question)
    session['asked_questions'] = asked_questions

    return render_template("quiz.html", question=left_side)

def check_answer():
    user_answer = request.form.get("answer")
    question = request.form.get("question")
    full_equation = next((eq for eq in session['equations'] if eq.startswith(question)), None)

    result = "Error: Question not found"
    if full_equation:
        expected_answer = full_equation.split('=')[1].strip()
        if user_answer == expected_answer:
            result = "Correct Answer"
            session['score'] += 1
        else:
            result = "Incorrect"

    session['questions_answered'] += 1
    if session['questions_answered'] == 10:
        return render_template("quiz.html", quiz_completed=True, score=session['score'])
    
    return render_template("quiz.html", question=question, result=result, answer_checked=True)