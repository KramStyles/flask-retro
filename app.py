from flask import Flask

app = Flask(__name__)
app.debug = True
app.env = 'development'

@app.route('/')
def home():
    return '<h2>Welcome to Flask Intro</h2>'

if __name__ == '__main__':
    app.run(debug=True)