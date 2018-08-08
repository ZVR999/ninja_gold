from flask import Flask, session, redirect, render_template, request
import random, datetime
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
    addAmount = 0
    where = '' 
    if building == 'farm':
        where = 'farm! '
        addAmount = random.randint(10,20)
        session['counter'] += addAmount
    elif building == 'cave':
        where = 'cave! '
        addAmount = random.randint(5,10)
        session['counter'] += addAmount
    elif building == 'house':
        where = 'house! '
        addAmount = random.randint(2,5)
        session['counter'] += addAmount
    elif building == 'casino':
        where = 'casino! '
        addAmount = random.randint(-50,50)
        session['counter'] += addAmount
    if 'activity' not in session:
        session['activity'] = ''
    earned = '<div>Earned '
    addedAmount = str(addAmount)
    gold = ' golds from the '
    # add where next
    dateEntered = datetime.datetime.now()
    current = str(dateEntered.year)+'</div>'
    session['activity'] += "{}{}{}{}{}".format(earned,addedAmount,gold,where,current)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    session['activity'] = ''
    return redirect('/')
app.run(debug=True)