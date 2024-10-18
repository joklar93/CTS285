import random
from flask import session, render_template, request

def number_guesser():
    if 'number' not in session:
        session['number'] = random.randint(0, 99)
        session['attempts'] = 8

    message = ""
    if request.method == "POST":
        guess = int(request.form.get("guess"))
        if guess == session['number']:
            message = "Congratulations! You guessed the correct number."
            session.pop('number', None)
        else:
            session['attempts'] -= 1
            if session['attempts'] == 0:
                message = f"You're out of attempts! The number was {session['number']}."
                session.pop('number', None)
            else:
                difference = abs(session['number'] - guess)
                hint = "higher" if guess < session['number'] else "lower"
                if difference <= 10:
                    message = f"You're close! Try guessing {hint}. Attempts left: {session['attempts']}"
                else:
                    message = f"More than 10 away! Try guessing {hint}. Attempts left: {session['attempts']}"

    return render_template("number_guesser.html", message=message)

def reset_game():
    session.pop('number', None)
    session.pop('attempts', None)
    return redirect(url_for('number_guesser'))