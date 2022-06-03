# import requests
# import matplotlib.pyplot as plt
# import math
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as py
from datetime import date
import yfinance as yf


start = '2015-01-01'
today = date.today().strftime("%Y-%m-%d")

st.title("Stock Predictions")

callSign = st.text_input('Stock Ticker Symbol', value = 'tsla')


@st.cache
def load_data():
    data = yf.download(callSign, start, today)
    data.reset_index(inplace = True)
    return data

data = load_data()

st.subheader(callSign + ' data')
st.write(data.tail())



df = pd.DataFrame({'time':timeStamp, 'price':priceData})
fig = px.line(df, x="time", y="price", title=callSignDispaly + " Stock Prices") 
# fig.show()


# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={callSign}&outputsize=compact&apikey=1TON9HITVA38HZQ5'
# r = requests.get(url)
# data = r.json()

# priceData = []
# timeStamp = []
# count = 0
# for each in data["Weekly Time Series"]:
#     if count < 10:
#         timeStamp.append(each)
#         priceData.append(math.floor(int(float(data["Weekly Time Series"][each]["1. open"]))))
#         count +=1

# callSignDispaly = callSign.upper()
# chartTitle = callSignDispaly + " Stock Prices"
# plt.plot(timeStamp, priceData, color='red', marker='o')
# plt.title(chartTitle, fontsize=14)
# plt.xlabel('Time', fontsize=14)
# plt.ylabel('Price', fontsize=14)
# plt.grid(True)
# plt.show()

# df = pd.DataFrame({'time':timeStamp, 'price':priceData})
# fig = px.line(df, x="time", y="price", title=callSignDispaly + " Stock Prices") 
# # fig.show()


# st.plotly_chart(fig, use_container_width=True)


# st.write('The current movie title is', callSign)