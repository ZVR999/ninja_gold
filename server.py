from flask import Flask, session, redirect, render_template, request
import random
app = Flask(__name__)
app.secret_key = 'n1312rn23!@123!%^VDSDSdgge5#$hfdss#$646u4'

@app.route('/')
def index():
    # Adds counter to top most box
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    print request.form['building'] 
    if building == 'farm':
        session['counter'] += random.randint(10,20)
    

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')
app.run(debug=True)