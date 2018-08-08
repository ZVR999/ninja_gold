from flask import Flask, session, redirect, render_template, request
import random
import datetime
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
    #print request.form['building']
    addAmount = 0
    where = ''
    
    # Start of what to add to where and what to add to counter
    if building == 'farm':
        where = 'farm! '
        addAmount = random.randint(10, 20)
        session['counter'] += addAmount
    elif building == 'cave':
        where = 'cave! '
        addAmount = random.randint(5, 10)
        session['counter'] += addAmount
    elif building == 'house':
        where = 'house! '
        addAmount = random.randint(2, 5)
        session['counter'] += addAmount
    elif building == 'casino':
        where = 'casino! '
        addAmount = random.randint(-50, 50)
        session['counter'] += addAmount
    if 'activity' not in session:
        session['activity'] = ''
    # End of what to add to where and what to add to counter
    
    # Start of what to add to session[activity]
    earned = '<div>Earned '
    addedAmount = str(addAmount)
    gold = ' golds from the '
    dateEntered = datetime.datetime.now()
    current = '('+str(dateEntered.strftime('%Y/%m/%d %I:%M %p'))+')</div>'

    if building == 'casino':
        if addAmount >= 0:
            earned = '<div class="green">Entered a casino and won '
            where += 'Nice! '
        elif addAmount < 0:
            earned = '<div class="red">Entered a casino and lost '
            where += '...Ouch.. '
    # End of what to add to session[activity]  
    session['activity'] = "{}{}{}{}{}".format(
        earned, addedAmount, gold, where, current)
    
    # Create an array to hold session['activity']'s history
    if 'array' not in session:
        session['array'] = []
    # Add session['activity']'s history to session['array']
    session['array'] = list(session['array'])
    session['array'].append(session['activity'])
    # print session['array']
    # print len(session['array'])
    # Reverse the history in session['array'] so the last pops up on top of
    # The Activites box
    if len(session['array']) > 1:
        def revese(arr):
            for x in range(0,1):
                arr.insert(0,arr[-1])
                arr.pop()
            return arr            

        revese(session['array'])
    session['array'] = ''.join(session['array'])

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    session['activity'] = ''
    session['array'] = ''
    return redirect('/')


app.run(debug=True)
