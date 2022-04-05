from flask import Flask,render_template,request
import joblib
import numpy as np

reg = joblib.load('iplmodel.sav')

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('page.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    arr =[]
    if request.method == 'POST':

        temp_array = list()
        print(temp_array)

        #Batting Team
        batting_team = request.form['batting_team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
             temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        print(temp_array)
        # Bowling Team
        bowling_team = request.form['bowling_team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        print(temp_array)

        if(batting_team==bowling_team):
            return render_template('result.html',val="Batting and Bowling teams should be different.")

        overs = request.form['overs']
        runs = request.form["runs"]
        wickets =request.form["wickets"]
        runs_in_prev_5 = request.form["runs_in_prev_5"]
        wickets_in_prev_5 =request.form["wickets_in_prev_5"]

        if(batting_team =='none' or bowling_team=='none' or overs==''or runs==''or wickets==''or runs_in_prev_5==''or wickets_in_prev_5==''):
            return render_template('result.html',val='All fields should be filled.')

        overs  = float(overs)
        runs = int(runs)
        wickets = int(wickets)
        runs_in_prev_5 = int(runs_in_prev_5)
        wickets_in_prev_5 = int(wickets_in_prev_5)

        # Overs, Runs, Wickets, Runs_in_last_5, Wickets_in_last_5
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        print(temp_array)
        # Converting into numpy array
        temp_array = np.array([temp_array])
        print(temp_array)

        data = np.array([temp_array])
        print(data)
        pred = int(reg.predict(data[0]))
        print(pred)
        return render_template('result.html',val=f'The score will be from {pred +5} to {pred + 10}')

    
if __name__ == '__main__':
    app.run(debug=True)