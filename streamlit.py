import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go


def show_fig1():
    selected_feature = st.selectbox('Select Feature:', ['Age', 'Flight Distance', "Total score","Class","Customer Type"])
    age = dict(df[selected_feature].value_counts().sort_values())
    fig = go.Figure([go.Bar(x=list(age.keys()), y=list(age.values()))])
    fig.update_layout(
        xaxis_title=selected_feature, 
        yaxis_title='Number of people',  
    )
    st.plotly_chart(fig)
    
def show_fig2():
    fig2 = px.histogram(df, x="Age", color="satisfaction",
                        color_discrete_sequence=px.colors.qualitative.Antique)
    fig2.update_layout(
        title="<b>Age Distribution by Satisfaction</b>",
        barmode="overlay"
    )
    fig2.update_layout(
        xaxis_title="Age", 
        yaxis_title='Number of people',  
    )
    fig2.update_traces(opacity=0.6)
    st.plotly_chart(fig2)
    
def show_fig3():
    fig3 = px.scatter(
        df,
        x="Flight Distance",
        y="Arrival Delay in Minutes",
        marginal_x="histogram",
        marginal_y="histogram",
        title="<b>Correlation between Flight Distance and Arrival Delay",
        color_discrete_sequence=px.colors.qualitative.Antique
    )
    st.plotly_chart(fig3)
def show_fig4():
    selected_feature = st.selectbox('Select Feature:', ["Gender", "Type of Travel","satisfaction"])
    gender_info = df[selected_feature].value_counts()
    pie_fig = go.Figure(data=[go.Pie(labels=gender_info.index, values=gender_info.values)])

    pie_fig.update_layout(
        title=selected_feature+" Distribution",
        barmode="overlay"
    )
    st.plotly_chart(pie_fig)


#Uploading data
df = pd.read_csv("train.csv")
df["Total score"] = df[["Inflight wifi service","Departure/Arrival time convenient","Ease of Online booking","Gate location","Food and drink","Online boarding","Seat comfort","Inflight entertainment","On-board service","Leg room service","Baggage handling","Inflight service","Cleanliness","Checkin service"]].sum(axis=1)
df = df.drop(df.columns[[0,1]],axis=1)
df.dropna(subset="Arrival Delay in Minutes",inplace=True)
df.loc[df["Customer Type"] == "disloyal Customer", "Customer Type"] = "Disloyal Customer"

#Making main article
st.title('Airline Passenger Satisfaction')

#Sidebar
sidebar = st.sidebar
selected_option = st.sidebar.selectbox('Select Visualization', ["Info",'Histograms', 'Age Distribution', 'Correlation', 'Pie Charts'])
if selected_option == "Info":
    st.markdown("Dataset contains an airline passenger satisfaction survey.")
    st.subheader("Dataset statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        _value = df.shape[0]
        st.metric(label="Number of passenger", value=_value)
    with col2:
        _value = df.shape[1]
        st.metric(label="Number of columns", value=_value)  
elif selected_option == "Histograms":
    show_fig1()
elif selected_option == "Age Distribution":
    show_fig2()
elif selected_option == "Correlation":
    show_fig3()
elif selected_option == "Pie Charts":
    show_fig4()
else:
    st.write("Please choose a table from the sidebar.")

    
    
    

    