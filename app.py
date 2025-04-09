from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)