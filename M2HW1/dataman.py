# CTS 285
# M2HW1
# James Reynolds
# 09/21/2024
import random, re, logging, traceback
from flask import Flask, render_template, request, session, redirect, url_for, jsonify


app = Flask(__name__)
app.secret_key = 'thepanthersarenevergoingtowinasuperbowlinmylifetime'
app.config["DEBUG"] = True

logging.basicConfig(level=logging.DEBUG)


def validate_equation(equation: str) -> bool:
    pattern = r'^\d{1,2}\s*[\+\-\*/]\s*\d{1,2}\s*=\s*\d{1,3}$'
    if not re.match(pattern, equation):
        return False
    
    left, right = equation.split('=')
    try:
        result = eval(left.strip())
        return result == int(right.strip())
    except:
        return False

def evaluate_equation(equation: str) -> str:
    try:
        problem, expected_answer = equation.split('=')
        expected_answer = int(expected_answer.strip())
        
        result = eval(problem.strip())
        
        if result == expected_answer:
            return "- - — - - = - - - ◌"
        else:
            return "EEE"
        
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("main_page.html")

@app.route("/answer_checker", methods=["GET", "POST"])
def answer_checker():
    comment = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("equation", "")
        comment = evaluate_equation(user_input)
    return render_template("answer_checker.html", comment=comment, user_input=user_input)

@app.route("/memory_bank", methods=["GET", "POST"])
def memory_bank():
    if request.method == "POST":
        try:
            equations = []
            for i in range(10):
                equation = request.form.get(f"equation{i}")
                if equation and validate_equation(equation):
                    equations.append(equation)
                elif equation:
                    return jsonify({"success": False, "error": f"Invalid equation: {equation}. Please enter a valid equation."})

            session['equations'] = equations
            session['asked_questions'] = []
            session['score'] = 0  # Reset score for new quiz
            session['questions_answered'] = 0
            logging.debug(f"Saved equations: {equations}")
            return jsonify({"success": True})
        except Exception as e:
            logging.error(f"Error in memory_bank: {str(e)}")
            logging.error(traceback.format_exc())
            return jsonify({"success": False, "error": "An unexpected error occurred. Please try again."})
        
    show_form = request.args.get('show_form', 'false').lower() == 'true'
    return render_template("memory_bank.html", equations=session.get('equations'), show_form=show_form)
  
@app.route("/validate_equation", methods=["POST"])
def validate_equation_route():
    equation = request.form.get("equation")
    is_valid = validate_equation(equation) if equation else False
    return jsonify({"valid": is_valid})


@app.route("/quiz")
def quiz():
    if 'equations' not in session or not session['equations']:
        return redirect(url_for('memory_bank'))

    # Initialize score at the beginning of the quiz
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

@app.route("/check_answer", methods=["POST"])
def check_answer():
    user_answer = request.form.get("answer")
    question = request.form.get("question")
    full_equation = next((eq for eq in session['equations'] if eq.startswith(question)), None)

    result = "Error: Question not found"
    if full_equation:
        expected_answer = full_equation.split('=')[1].strip()
        if user_answer == expected_answer:
            result = "- - — - - = - - - ◌"
            session['score'] += 1  #
        else:
            result = "EEE"

    session['questions_answered'] += 1
    if session['questions_answered'] == 10:
        return render_template("quiz.html", quiz_completed=True, score=session['score'])
    
    return render_template("quiz.html", question=question, result=result, answer_checked=True)

if __name__ == "__main__":
    app.run()
    

