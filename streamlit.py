import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt

# Загрузка данных
st.title('Airline Passenger Satisfaction')
df = pd.read_csv("train.csv")

#Age distribution
num_bins = st.slider('Select number of bins:', min_value=25, max_value=75, value=20)
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Age"], kde=True, bins=num_bins, edgecolor="black", color="skyblue")
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)
ax.set_title('Age Distribution', fontsize=16)
ax.legend(labels=['Age Distribution'], loc='upper right')
info_box = f"Mean Age: {df['Age'].mean():.2f}\nMedian Age: {df['Age'].median()}\nMax Age: {df['Age'].max()}"
st.sidebar.text(info_box)
st.pyplot(fig)
