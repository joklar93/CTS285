# v3 - uses actual database.
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email TEXT PRIMARY KEY, password TEXT)''')
    c.execute('INSERT OR IGNORE INTO users VALUES (?, ?)',
              ('admin@example.com', 'admin123'))
    conn.commit()
    conn.close()

def verify_login(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email=? AND password=?', 
              (email, password))
    result = c.fetchone()
    conn.close()
    return result is not None

@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        if verify_login(request.form['email'], request.form['password']):
            message = "Login successful!"
        else:
            message = "Invalid credentials"
    return render_template_string(LOGIN_TEMPLATE, message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)