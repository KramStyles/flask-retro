from flask import Flask, render_template, request, g, session
from secrets import token_urlsafe

from model import User

app = Flask(__name__)
app.debug = True
app.env = 'development'
app.secret_key = token_urlsafe(24)


@app.route('/')
def home():
    return render_template('index.html')


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
        print('Password:', password)
        if password.strip() == '':
            msg = 'Password should not be empty'
        if confirm != password:
            msg = 'Passwords do not match'
        else:
            msg = 'supposed to create'
            # msg = profile.create(f"'{user}', '{password}', 'Null'")
    return f'<h2>{msg}</h2>'

@app.route('/login')
def login():
    pass

@app.route('/sign_in')
def sign_in():
    g.current = user
    session['username'] = user
    print(session)
    return g.get('current')
    pass


@app.route('/grid_1')
def grid():
    return render_template('grid_1.html')


@app.route('/grid_2')
def grid_2():
    return render_template('grid_2.html')


if __name__ == '__main__':
    app.run(debug=True)
