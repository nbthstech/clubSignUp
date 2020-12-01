import pandas as pd
from flask import render_template

def names_function(name):
    try:
        message = f"Hello, your name is {name}"
        return render_template('namesOutput.html', message=message)
    except Exception as e:
        return render_template('error.html', e=e)
