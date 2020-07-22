# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:45:56 2020

@author: Niteesh
"""

from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

pickle_in = open('ipl-prediction-lr-model.pkl', 'rb')
model = pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    bat_array = list()
    bowl_array = list()

    if request.method == 'POST':

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            bat_array = bat_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            bat_array = bat_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            bat_array = bat_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            bat_array = bat_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            bat_array = bat_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            bat_array = bat_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            bat_array = bat_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            bat_array = bat_array + [0,0,0,0,0,0,0,1]


        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            bowl_array = bowl_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            bowl_array = bowl_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            bowl_array = bowl_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            bowl_array = bowl_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            bowl_array = bowl_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            bowl_array = bowl_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            bowl_array = bowl_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            bowl_array = bowl_array + [0,0,0,0,0,0,0,1]


        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        final_array = [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5] + bat_array + bowl_array

        data = np.array([final_array])
        my_prediction = int(model.predict(data)[0])

        return render_template('index.html', my_prediction=my_prediction, lower_limit = my_prediction-5, upper_limit = my_prediction+10, batting_team=batting_team)


if __name__ == '__main__':
    app.run(debug=True)
