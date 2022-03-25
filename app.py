from flask import Flask, render_template, request

from model import User

app = Flask(__name__)
app.debug = True
app.env = 'development'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check')
def check():
    print(User('').get_users())
    return 'Something'


@app.route('/home_form', methods=['POST'])
def home_request():
    users = ['karm_designs', 'karm']
    user = request.form['username']
    password = request.form.get('password')
    if user in users:
        # Todo: Fix cannot connect to database error
        profile = User(user)
        return profile.get_fav_color()
    return f"({user}, {password})"


@app.route('/grid_1')
def grid():
    return render_template('grid_1.html')


@app.route('/grid_2')
def grid_2():
    return render_template('grid_2.html')


if __name__ == '__main__':
    app.run(debug=True)
