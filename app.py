from flask import Flask, render_template, request, g, session, redirect, url_for
from secrets import token_urlsafe

from model import User

app = Flask(__name__)
app.debug = True
app.env = 'development'
app.secret_key = token_urlsafe(24)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signin')
def login():
    return render_template('login.html')

@app.route('/reg')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/check')
def check():
    print(User('').get_users())
    return 'Something'


@app.route('/home_form', methods=['POST'])
def home_request():
    user = request.form['username']
    profile = User(user)
    password = request.form.get('password')
    confirm = request.form.get('confirm')
    msg = 'User already exists in database'
    if not profile.check_user_exists():
        if password.strip() == '':
            msg = 'Password should not be empty'
        elif confirm != password:
            msg = 'Passwords do not match'
        else:
            msg = profile.create(f"'{user}', '{password}', 'Null'")
    return f'<h2>{msg}</h2>'


@app.route('/sign_in', methods=['POST'])
def sign_in():
    user = request.form['username']
    profile = User(user)
    password = request.form.get('password')
    msg = "User not registered"
    if profile.check_user_exists():
        if profile.authenticate(user, password):
            g.current = user
            session['username'] = g.get('current')
            print(session)
            return redirect(url_for('home'))
        else: msg = "Invalid Authentication"
    return f'<h2>{msg}</h2>'


@app.route('/grid_1')
def grid():
    return render_template('grid_1.html')


@app.route('/grid_2')
def grid_2():
    return render_template('grid_2.html')


if __name__ == '__main__':
    app.run(debug=True)
