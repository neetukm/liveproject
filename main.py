import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# read the file

st.set_page_config(layout="wide")

df = pd.read_csv("Shark Tank India Dataset.csv")
df.head()
# Title
st.title('Sharks')
st.header('Investment ')

# subheader show rainbow color
st.subheader(':rainbow[Deal of the shark]')
tab1,tab2,tab3,tab4= st.tabs(['summary','Top and Bottom Rows','Data Types','Columns'])

with tab1:
    st.write(f"There are {df.shape[0]} rows in dataset and {df.shape[1]} columns in the dataset")
    st.subheader(':gray[statistical summary of the dataset]')
    st.dataframe(df.describe())

with tab2:
    st.subheader(':gray[Top Rows]')
    st.dataframe(df.head(6))

with tab3:
    st.subheader(':gray[Data types of column]')
    st.dataframe(df.dtypes)

with tab4:
    st.subheader('Column Names in Dataset')
    st.dataframe(df.columns)



st.subheader(':rainbow[Show all data]')

# Select columns for grouping
st.subheader(':rainbow[Every episode number is count deal with deal amount]')
st.dataframe(df)
groupby_column = st. selectbox(
    'What would you like?',
    ('episode_number', 'deal', 'deal_amount', 'pitcher_ask_amount',	'ask_equity',	'ask_valuation')
)

# Gruop by column in DataFrame


summary = df[df['deal'] == 1].groupby('episode_number').agg(total_deal_amount=('deal_amount', 'sum'),deal_count=('deal', 'count')).reset_index()
st.dataframe(summary)
plt.figure(figsize=(10, 6))
plt.plot(summary['episode_number'], summary['total_deal_amount'], marker='o', label='Total Deal Amount')
plt.plot(summary['episode_number'], summary['deal_count'], marker='s', label='Deal Count')

# Step 3: Customize the plot
st.line_chart(summary)



