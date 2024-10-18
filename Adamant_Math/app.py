import random, re, logging, traceback
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from answer_checker import validate_equation, evaluate_equation
from memory_bank import memory_bank, validate_equation_route
from quiz import quiz, check_answer, reset_quiz
from number_guesser import number_guesser, reset_game
from number_memory import number_memory, reset_game

app = Flask(__name__)
app.secret_key = 'thepanthersarenevergoingtowinasuperbowlinmylifetime'
app.config["DEBUG"] = True

logging.basicConfig(level=logging.DEBUG)

#If quiz question does not work try:
#app.jinja_env.globals.update(QUESTIONS_PER_QUIZ=10)

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

app.route("/memory_bank", methods=["GET", "POST"])(memory_bank)
app.route("/validate_equation", methods=["POST"])(validate_equation_route)
app.route("/quiz", methods=['GET', 'POST'])(quiz)
@app.route("/reset_quiz")
def reset_quiz_route():
    return reset_quiz()
app.route("/check_answer", methods=["POST"])(check_answer)
app.route("/number_guesser", methods=["GET", "POST"])(number_guesser)
app.route("/reset_number_guesser")(reset_game)
app.route("/number_memory", methods=["GET", "POST"])(number_memory)
app.route("/reset_memory")(reset_game)

if __name__ == "__main__":
    app.run()