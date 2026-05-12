import streamlit as st
import pandas as pd
import pickle

pipe=pickle.load(open('pipe.pkl','rb'))

teams=[
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Punjab Kings'
]

cities=[
    'Mumbai',
    'Kolkata',
    'Delhi',
    'Chennai',
    'Bangalore',
    'Hyderabad'
]

st.title('IPL Win Predictor\n(***LAST 30 BALLS ONLY***)')

batting_team=st.selectbox('Batting Team',teams)

bowling_team=st.selectbox('Bowling Team',teams)

city=st.selectbox('City',cities)

target=st.number_input('Target')

score=st.number_input('Current Score')

overs=st.number_input('Overs Completed')

wickets=st.number_input('Wickets Out')

if st.button('Predict Probability'):

    runs_left=target-score

    balls_left=120-(overs*6)

    wickets_left=10-wickets

    crr=score/overs

    rrr=(runs_left*6)/balls_left

    input_df=pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets_left':[wickets_left],
        'runs_target':[target],
        'crr':[crr],
        'rrr':[rrr]
    })

    result=pipe.predict_proba(input_df)

    loss=result[0][0]
    win=result[0][1]

    st.header(batting_team+" Win Probability : "+str(round(win*100))+"%")
    st.header(bowling_team+" Win Probability : "+str(round(loss*100))+"%")
