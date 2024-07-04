from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def loading():
    return render_template("animetion.html")

@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/academic')
def academic():
    return render_template("academic.html")

@app.route('/admission')
def admission():
    return render_template("admission.html")

app.run(debug=True)
