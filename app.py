from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def GoToResults():
    query = request.args.get("query", "")
    return render_template('results.html', query=query)

if __name__ == "__main__":
    app.run(debug=True, port=8000)