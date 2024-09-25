# CTS 285
# M2HW1
# James Reynolds
# 09/21/2024
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True

def evaluate_equation(equation: str) -> str:
    try:
        problem, expected_answer = equation.split('=')
        expected_answer = int(expected_answer.strip())

        result = eval(problem.strip())

        if result == expected_answer:
            return "Correct!"
        elif result > expected_answer:
            return "Answer too low."
        else:
            return "Answer too high."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    comment = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("equation", "")
        comment = evaluate_equation(user_input)
    return render_template("main_page.html", comment=comment, user_input=user_input)

if __name__ == "__main__":
    app.run()
    

