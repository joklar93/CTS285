import logging, traceback
from flask import render_template, request, session, jsonify
from answer_checker import validate_equation

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
            session['score'] = 0
            session['questions_answered'] = 0
            logging.debug(f"Saved equations: {equations}")
            return jsonify({"success": True})
        except Exception as e:
            logging.error(f"Error in memory_bank: {str(e)}")
            logging.error(traceback.format_exc())
            return jsonify({"success": False, "error": "An unexpected error occurred. Please try again."})
        
    show_form = request.args.get('show_form', 'false').lower() == 'true'
    return render_template("memory_bank.html", equations=session.get('equations'), show_form=show_form)

def validate_equation_route():
    equation = request.form.get("equation")
    is_valid = validate_equation(equation) if equation else False
    return jsonify({"valid": is_valid})