from app.getNames import names_function
from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/names/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        name = request.form['name']
        return names_function(name)
    return render_template('names.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)