# minimal Flask app
from flask import Flask, render_template, request, redirect, url_for

#print("Starting flask program from ", __name__)
app = Flask(__name__)
# Do any app specific setup here
# for instance, loading a database
app.config["DEBUG"] = True # will run in debug mode
# TODO: make this a database or something
comments = []

@app.route("/", methods=["GET", "POST"]) # we allow posting
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    #otherwise, it's a post
    comments.append(request.form["contents"])
    return redirect(url_for('index'))
    
@app.route("/action")
def action():
    return "Hello from the action route!"