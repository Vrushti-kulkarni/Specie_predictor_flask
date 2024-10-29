#flask app routing

from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('decision_tree.pkl','rb'))
#simple basic app
app = Flask(__name__) #flask app denoted by app variable name, this is the entry point of my program

#to make a specific route
@app.route("/", methods=["GET"])
def main():
    return render_template('main.html')

@app.route("/index", methods=["POST"])
def home():
    island = request.form['a']
    bill_length_mm = request.form['b']
    bill_depth_mm = request.form['c']
    flipper_length_mm = request.form['d']
    body_mass_g = request.form['e']
    sex = request.form['f']
    year = request.form['g']
    input_data = pd.DataFrame({
        'island': [island],
        'bill_length_mm': [bill_length_mm],
        'bill_depth_mm': [bill_depth_mm],
        'flipper_length_mm': [flipper_length_mm],
        'body_mass_g': [body_mass_g],
        'sex': [sex],
        'year': [year]
    })
    prediction = model.predict(input_data)
    return render_template('after.html', data=prediction)

if __name__=="__main__":
    app.run(debug=True) #debug is true automatically updates the webapp if any change in code