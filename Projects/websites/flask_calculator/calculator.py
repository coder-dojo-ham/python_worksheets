from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to my calculator app. Go to / for calculations'


@app.route('/number/<int:number>')
def show_number(number):
    return 'You asked for the number {}'.format(number)


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)


@app.route('/add-html/<int:num1>/<int:num2>')
def add_html(num1, num2):
    return render_template('html-add.html', num1=num1, num2=num2, result=num1 + num2)


@app.route('/add_post', methods=['POST'])
def add_post():
    return str(int(request.form['num1']) + int(request.form['num2']))


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')
