from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.env = 'development'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grid_1')
def grid():
    return render_template('grid_1.html')

@app.route('/grid_2')
def grid_2():
    return render_template('grid_2.html')

if __name__ == '__main__':
    app.run(debug=True)