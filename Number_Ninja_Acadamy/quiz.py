import random
from flask import render_template, request, session, redirect, url_for

def quiz():
    if 'reset_quiz' in request.args:
        _clear_quiz_session()
        session['score'] = 0
        session['questions_answered'] = 0
        session['equations'] = session.get('equations', [])
        return redirect(url_for('quiz'))
    
    equations = session.get('equations', [])
    questions_answered = session.get('questions_answered', 0)
    
    if questions_answered >= 10:
        score = session.get('score', 0)
        quiz_completed = True
        return render_template("quiz.html", quiz_completed=quiz_completed, score=score)

    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = eval(session['equations'][questions_answered].split('=')[0].strip())
        
        if int(user_answer) == correct_answer:
            session['score'] += 1
            
        session['questions_answered'] += 1
        return redirect(url_for('quiz'))

    if questions_answered < len(equations):
        question = session['equations'][questions_answered].split('=')[0]
        return render_template("quiz.html", question=question, question_number=questions_answered + 1, answer_checked=False)

    return redirect(url_for('memory_bank', show_form=True))

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
    question_number = session['questions_answered'] + 1

    if session['questions_answered'] == 10:
        return render_template("quiz.html", quiz_completed=True, score=session['score'])
    
    return render_template("quiz.html", question=question, result=result, answer_checked=True, question_number=question_number)

def reset_quiz():
    _clear_quiz_session()
    session['score'] = 0
    session['questions_answered'] = 0
    return redirect(url_for('quiz'))

def _clear_quiz_session():
    session.pop('score', None)
    session.pop('questions_answered', None)
    session.pop('asked_questions', None)