from flask import Flask, session, redirect, render_template
app = Flask(__name__)
app.secret_key = 'n1312rn23!@123!%^VDSDSdgge5#$hfdss#$646u4'

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)