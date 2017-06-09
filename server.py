from flask import Flask , render_template, redirect, session, request
import random, datetime
app=Flask(__name__)
app.secret_key="1234"
@app.route('/')
def index():
    if 'list' not in session.keys():
        session['list']=[]
    if 'total' not in session.keys():
        session['total']=0
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def calculate():
    session['class']='green'
    session['time']=time=datetime.datetime.now()
    if request.form['submit']=='farm':
        session['take_away']=random.randrange(10,21)
        session['total']+=session['take_away']
        print request.form['submit']
    elif request.form['submit']=='cave':
        session['take_away']=random.randrange(5,11)
        session['total']+=session['take_away']
        print session['total']
    elif request.form['submit']=='house':
        session['take_away']=random.randrange(2,6)
        session['total']+=session['take_away']
        print session['total']
    elif request.form['submit']=='casino':
        session['take_away']=random.randrange(0,51)
        #3/8 chance of loosing
        if random.randrange(1,8)< 4:
            session['class']='red'
            session['total']-=session['take_away']
        else:
            session['total']+=session['take_away']
        print session['total']
    session['win']="Earned " +str(session['total'])+ " golds from the " + request.form['submit']+" ! " + str(session['time'])
    session['lost']="Entered a casino and lost" +str(session['total'])+ "golds...ouch.." + str(session['time'])
    if session['class']=='red':
        session['list']+=[[session['lost'],session['class']]]
    else:
        session['list']+=[[session['win'],session['class']]]
    print session['list'][0]
    return redirect('/')
@app.route('/reset')
def reset():
    session.pop('win')
    session.pop('lost')
    session.pop('list')
    session.pop('take_away')
    session.pop('total')
    return redirect('/')
app.run(debug=True)
