# CTS 285
# M2HW1
# James Reynolds
# 09/21/2024
import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'thepanthersarenevergoingtowinasuperbowlinmylifetime'
app.config["DEBUG"] = True

def evaluate_equation(equation: str) -> str:
    try:
        problem, expected_answer = equation.split('=')
        expected_answer = int(expected_answer.strip())

        result = eval(problem.strip())

        if result == expected_answer:
            return "- - — - - = - - - ◌"
        else: return "EEE"
        
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
        equations = []
        for i in range(10):
            equation = request.form.get(f"equation{i}")
            if equation:
                equations.append(equation)
        session['equations'] = equations
        return render_template("memory_bank.html", equations=equations)
    return render_template("memory_bank.html", equations=session.get('equations'))

@app.route("/quiz")
def quiz():
    if 'equations' not in session or not session['equations']:
        return redirect(url_for('memory_bank'))
    
    equations = session['equations']
    question = random.choice(equations)
    left_side = question.split('=')[0]
    
    return render_template("quiz.html", question=left_side)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    user_answer = request.form.get("answer")
    question = request.form.get("question")
    full_equation = next((eq for eq in session['equations'] if eq.startswith(question)), None)
    
    if full_equation:
        expected_answer = full_equation.split('=')[1].strip()
        if user_answer == expected_answer:
            result = "- - — - - = - - - ◌"
        else:
            result = "EEE"
    else:
        result = "Error: Question not found"

    return render_template("quiz.html", question=question, result=result)

if __name__ == "__main__":
    app.run()
    

