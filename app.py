from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
# Flask app initialize
app = Flask(__name__)

# Load trained model
# tset
model = pickle.load(open("Students_Marks_predict_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
            hours = float(request.form['hours'])
            prediction = model.predict([[hours]])
            predicted_marks = round(prediction[0], 2)
            return render_template("index.html", prediction=predicted_marks)

if __name__ == '__main__':
    app.run(debug=True)
