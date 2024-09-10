import streamlit as st
import pandas as pd
import sqlite3

st.title('Welcome to SoolyTech homepages')

st.write('Buffered 전략')
conn= sqlite3.connect('soolyDB.db')

sql_query = pd.read_sql_query(
    '''
    select * from his_data where name = '삼성전자';
    ''',
    conn
)

df = pd.DataFrame(sql_query)

chart_data = pd.DataFrame(df.head(20), columns=["date", "close"])

st.subheader('삼성전자 주가')

st.line_chart(chart_data, x="date", y="close")
