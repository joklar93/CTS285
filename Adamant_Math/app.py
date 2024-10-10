
import random, re, logging
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from answer_checker import validate_equation, evaluate_equation
from memory_bank import memory_bank, validate_equation_route
from quiz import quiz, check_answer

app = Flask(__name__)
app.secret_key = 'thepanthersarenevergoingtowinasuperbowlinmylifetime'
app.config["DEBUG"] = True

logging.basicConfig(level=logging.DEBUG)

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
app.route("/quiz")(quiz)
app.route("/check_answer", methods=["POST"])(check_answer)

if __name__ == "__main__":
    app.run()