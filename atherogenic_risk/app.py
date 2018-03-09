from atherogenic_risk import app
from flask import render_template, request, redirect
from atherogenic_risk.forms import PrimaryForm


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


if __name__ == '__main__':
    app.run()
