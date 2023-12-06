import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
df["Total score"] = df[["Inflight wifi service","Departure/Arrival time convenient","Ease of Online booking","Gate location","Food and drink","Online boarding","Seat comfort","Inflight entertainment","On-board service","Leg room service","Baggage handling","Inflight service","Cleanliness","Checkin service"]].sum(axis=1)

st.title('Airline Passenger Satisfaction')

#Histogram
selected_feature = st.selectbox('Select Feature:', ['Age', 'Flight Distance', "Total score"])

num_bins = st.slider('Select number of bins:', min_value=25, max_value=75, value=55)
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df[selected_feature], kde=True, bins=num_bins, edgecolor="black", color="skyblue")
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_xlabel(selected_feature, fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)
ax.set_title(f'{selected_feature} Distribution', fontsize=16)
st.pyplot(fig)
