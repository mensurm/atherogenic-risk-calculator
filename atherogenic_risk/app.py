from atherogenic_risk import app
from flask import render_template, request, redirect


@app.route('/')
def index():
    return redirect('/first-step')

@app.route('/first-step', methods=['GET', 'POST'])
def first_step():
    if request.method == 'GET':
        return render_template('first-step.html')

    tc = request.form['cholesterol']
    tg = request.form['triglyceride']
    hdl = request.form['lipoproteins']

    return render_template('second-step.html')

if __name__ == '__main__':
    app.run()
