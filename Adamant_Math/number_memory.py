import random
from flask import session, render_template, request, redirect, url_for

def number_memory():
    if 'sequence' not in session:
        session['sequence'] = [str(random.randint(0, 9))]
        session['current_step'] = 1

    message = ""
    displayed_sequence = ' '.join(session.get('sequence', []))
    
    if request.method == "POST":
        user_input = request.form.get("user_input")
        sequence = session['sequence']
        current_step = session['current_step']

        if user_input == ''.join(sequence):
            if current_step == 10:
                message = "Congratulations! You've memorized all 10 numbers!"
                session.pop('sequence')
                session.pop('current_step')
            else:
                session['sequence'].append(str(random.randint(0, 9)))
                session['current_step'] += 1
                return redirect(url_for('number_memory'))
        else:
            message = f"Incorrect! The sequence was {''.join(sequence)}."
            session.pop('sequence')
            session.pop('current_step')

    return render_template("number_memory.html", message=message, sequence=displayed_sequence)

def reset_memory():
    session.pop('sequence', None)
    session.pop('current_step', None)
    return redirect(url_for('number_memory'))