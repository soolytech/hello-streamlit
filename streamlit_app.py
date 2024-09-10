import streamlit as st
import pandas as pd
import sqlite3


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.title('Welcome to SoolyTech homepages')

conn= sqlite3.connect('soolyDB.db')

sql_query = pd.read_sql_query(
    '''
    select * from his_data where name = 'SK하이닉스';
    ''',
    conn
)

df = pd.DataFrame(sql_query)

chart_data = pd.DataFrame(df.head(20), columns=["date", "close"])

st.subheader('SK 하이닉스 주가')

st.line_chart(chart_data, x="date", y="close")
