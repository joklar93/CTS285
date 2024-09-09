# M2T1 - Webapp #1

## goals:
- to learn basic Flask programming
- to be able to repeat a server config
- maybe to have fun

## leassons learned
bash commands you cannot live without:
- ls <-what's in this directory
- cd <- change directory
- source <- run a script (like activate)

## instructions
initial tutorial: https://blog.pythonanywhere.com/121/
but we're using codespaces instead of PA

install library:
pip install virtualenv
pip install flask

first set up virtualenvironment
- pip install virtualenv
- virtualenv venv
- source venv/bin/acvtivate
now we have our "venv" environment, so we can install things in it.

to turn it off:
-deactivate

start installing requirments:
- pip install flask
- pip freeze > requirements.txt
- pip freeze -r requirements.txt

now we can write our minimal flask app to test it
TODO: write a Flask app that does something useful!

to start:
-flask -app hello run

flask --debug --app hello run