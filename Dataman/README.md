# Dataman Calculator

## Change directories and get into a virtual environment
- cd M2HW1
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate

## Now install Flask and run the program in debug mode
- pip install flask
- flask --debug --app dataman run
- Click the open in browser on the bottom right pop up

## Stop the program
- Ctrl+c in the terminal

## Leave the virtual environment (type in terminal)
- deactivate

## If anything does not work
- Close the program browser and stop the program
- trying running in debug mode again with: flask --debug --app dataman run

## My ToDo's
- Clean up main page and change fonts
- Clean up navigation on games
- Fix input for answer checker - needs to be two 2 digits with at most 3 digit answer
- Get started on the number guesser (should not be too dificult)