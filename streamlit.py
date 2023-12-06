import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go

#Uploading data
df = pd.read_csv("train.csv")
df["Total score"] = df[["Inflight wifi service","Departure/Arrival time convenient","Ease of Online booking","Gate location","Food and drink","Online boarding","Seat comfort","Inflight entertainment","On-board service","Leg room service","Baggage handling","Inflight service","Cleanliness","Checkin service"]].sum(axis=1)
df = df.drop(df.columns[[0,1]],axis=1)
df.dropna(subset="Arrival Delay in Minutes",inplace=True)
df.loc[df["Customer Type"] == "disloyal Customer", "Customer Type"] = "Disloyal Customer"

#Making main article
st.title('Airline Passenger Satisfaction')

#Histograms

selected_feature = st.selectbox('Select Feature:', ['Age', 'Flight Distance', "Total score","Class","Customer Type"])
age = dict(df[selected_feature].value_counts().sort_values())
fig = go.Figure([go.Bar(x=list(age.keys()), y=list(age.values()))])
fig.update_layout(
    xaxis_title=selected_feature, 
    yaxis_title='Number of people',  
)
st.plotly_chart(fig)

st.markdown("---")


fig = px.histogram(df, x="Age", color="satisfaction",
                   color_discrete_sequence=px.colors.qualitative.Antique)
fig.update_layout(
    title="<b>Age Distribution by Satisfaction</b>",
    barmode="overlay"
)
fig.update_layout(
    xaxis_title="Age", 
    yaxis_title='Number of people',  
)
fig.update_traces(opacity=0.6)
st.plotly_chart(fig)

st.markdown("---")

#Scatter
fig = px.scatter(
    df,
    x="Flight Distance",
    y="Arrival Delay in Minutes",
    marginal_x="histogram",
    marginal_y="histogram",
    title="<b>Correlation between Flight Distance and Arrival Delay",
    color_discrete_sequence=px.colors.qualitative.Antique
)
st.plotly_chart(fig)

st.markdown("---")

#Pie
selected_feature = st.selectbox('Select Feature:', ["Gender", "Type of Travel","satisfaction"])
gender_info = df[selected_feature].value_counts()
pie_fig = go.Figure(data=[go.Pie(labels=gender_info.index, values=gender_info.values)])

pie_fig.update_layout(
    title=selected_feature+" Distribution",
    barmode="overlay"
)

st.plotly_chart(pie_fig)