from flask import render_template, request, redirect
from atherogenic_risk.forms import PrimaryForm
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/first-step')


@app.route('/first-step', methods=['GET'])
def first_step():
    form = PrimaryForm(request.form)
    return render_template('first-step.html', form=form)


@app.route('/first-step', methods=['POST'])
def submit_first_step():
    form = PrimaryForm(request.form)
    return render_template('second-step.html', form=form)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
