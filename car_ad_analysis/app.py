import  as st
import pandas as pd
import plotly.express as px

st.title("Car Advertisement Dashboard")

data = pd.read_csv('vehicles_us.csv')  

st.header("Exploratory Data Analysis of Car Advertisements")

st.subheader("Distribution of Vehicle Prices")
fig_price_hist = px.histogram(data, x='price', nbins=30, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_price_hist)

st.subheader("Price vs. Mileage")
fig_price_mileage = px.scatter(data, x='mileage', y='price', title='Price vs. Mileage', 
                                labels={'mileage': 'Mileage (in miles)', 'price': 'Price (in USD)'})
st.plotly_chart(fig_price_mileage)

if st.checkbox('Show DataFrame'):
    st.write(data)
else:
    st.write("DataFrame is hidden. Check the box to display it.")