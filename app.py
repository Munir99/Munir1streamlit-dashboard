import streamlit as st
import plotly.express as px
import csv

st.title("Car Advertisement Dashboard")

car_data = {
    'price': [],
    'model_year': [],
    'model': [],
    'condition': [],
    'cylinders': [],
    'fuel': [],
    'odometer': [],
    'transmission': [],
    'type': [],
    'paint_color': [],
    'is_4wd': [],
    'date_posted': [],
    'days_listed': []
}

# Use a relative path
with open('vehicles_us.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        car_data['price'].append(float(row['price']) if row['price'] else 0)
        car_data['odometer'].append(float(row['odometer']) if row['odometer'] else 0)
        
        # Convert model_year to float first, then to int
        car_data['model_year'].append(int(float(row['model_year'])) if row['model_year'] else 0)
        
        car_data['cylinders'].append(row['cylinders'])
        car_data['fuel'].append(row['fuel'])
        car_data['transmission'].append(row['transmission'])

st.header("Exploratory Data Analysis of Car Advertisements")

# Histograms
st.subheader("Distribution of Vehicle Prices")
fig_price_hist = px.histogram(x=car_data['price'], nbins=30, title="Vehicle Price Distribution", labels={'x': 'Price ($)'})
st.plotly_chart(fig_price_hist)

st.subheader("Distribution of Odometer Readings")
fig_odometer_hist = px.histogram(x=car_data['odometer'], nbins=30, title="Odometer Distribution", labels={'x': 'Odometer (miles)'})
st.plotly_chart(fig_odometer_hist)

st.subheader("Car Model Year Distribution")
fig_year_hist = px.histogram(x=car_data['model_year'], nbins=30, title="Model Year Distribution", labels={'x': 'Model Year'})
st.plotly_chart(fig_year_hist)

# Scatter Plots
st.subheader("Price vs. Odometer")
fig_price_odometer = px.scatter(x=car_data['odometer'], y=car_data['price'], color=car_data['fuel'],
                                 title="Price vs. Odometer", labels={'x': 'Odometer (miles)', 'y': 'Price ($)'})
st.plotly_chart(fig_price_odometer)

st.subheader("Price vs. Model Year")
fig_price_year = px.scatter(x=car_data['model_year'], y=car_data['price'], color=car_data['transmission'],
                             title="Price vs. Model Year", labels={'x': 'Model Year', 'y': 'Price ($)'})
st.plotly_chart(fig_price_year)

st.subheader("Odometer vs. Model Year")
fig_odometer_year = px.scatter(x=car_data['model_year'], y=car_data['odometer'], color=car_data['fuel'],
                                title="Odometer vs. Model Year", labels={'x': 'Model Year', 'y': 'Odometer (miles)'})
st.plotly_chart(fig_odometer_year)

# Raw data display
if st.checkbox('Show Raw Data'):
    st.write(car_data)
else:
    st.write("Raw data is hidden. Check the box to display it.")

