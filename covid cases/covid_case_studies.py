import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import os
files=os.listdir(r'C:\Users\Asutosh\Desktop\covid cases')
files
path=r'C:\Users\Asutosh\Desktop\covid cases'
def read_file(path,filename):
    return pd.read_csv(path + '/' + filename)
country_wise_group=read_file(path,files[0])
clean_data=read_file(path,files[1])
day_wise_data=read_file(path,files[2])
grouped_data=read_file(path,files[3])
usa_data=read_file(path,files[4])
world_data=read_file(path,files[5])
world_data.head()
world_data.columns
columns=['TotalCases','TotalDeaths','ActiveCases','TotalRecovered']
for i in columns:
    fig=px.treemap(data_frame=world_data.iloc[0:20],values=i,path=['Country/Region'],title="<b>TreeMap representation of different Countries w.r.t. their {}</b>".format(i))
    fig.show()
fig2=px.line(day_wise_data,x='Date',y=['Confirmed', 'Deaths', 'Recovered', 'Active'],title="covid cases w.r.t. date",template='plotly_dark')
fig2.show()
pop_test_ratio=world_data['Population']/world_data['TotalTests']
pop_test_ratio
fig3=px.bar(world_data.iloc[0:20],x='Country/Region',y=pop_test_ratio.iloc[0:20],color='Country/Region',title="<b>population to tests done ratio</b>")
fig3.show()
fig4=px.bar(world_data.iloc[0:20],x='Country/Region',y=['Serious,Critical','TotalCases','TotalRecovered','TotalDeaths','ActiveCases'])
fig4.update_layout({'title':"Coronavirus cases w.r.t. time"})
fig4.show()
cases=['TotalCases','TotalDeaths','ActiveCases','TotalRecovered']
for i in cases:
    fig5=px.bar(world_data.sort_values(by=i,ascending=False)[0:20],y=world_data['Country/Region'].iloc[0:20],x=i,color=i,text=i)
    fig5.update_layout(template='plotly_dark',title_text='top 20 countries of confirmed cases')
    fig5.show()
labels=world_data[0:15]['Country/Region'].values
cases=['TotalCases','TotalDeaths','ActiveCases','TotalRecovered']
for i in cases:
    fig7=px.pie(world_data[0:15],
               values=i,
               names=labels,
               hole=0.5,
               title=" {} Recordeded w.r.t. to WHO Region of 15 worst effected countries ".format(i))
    fig7.show()
death_to_confirmed=world_data['TotalDeaths']/world_data['TotalCases']
death_to_confirmed
fig8=px.bar(world_data,x=world_data['Country/Region'],y=death_to_confirmed)
fig8.show()
death_to_recovered=world_data['TotalDeaths']/world_data['TotalRecovered']
death_to_recovered
fig9=px.bar(world_data,x=world_data['Country/Region'],y=death_to_recovered)
fig9.show()
def country_visualization(grouped_data,country):
    
    data=grouped_data[grouped_data['Country/Region']==country]
    df=data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    fig = make_subplots(rows=1, cols=4,subplot_titles=("Confirmed", "Active", "Recovered",'Deaths'))
    fig.add_trace(
        go.Scatter(name="Confirmed",x=df['Date'],y=df['Confirmed']),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(name="Active",x=df['Date'],y=df['Active']),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name="Recovered",x=df['Date'],y=df['Recovered']),
        row=1, col=3
    )

    fig.add_trace(
        go.Scatter(name="Deaths",x=df['Date'],y=df['Deaths']),
        row=1, col=4
    )

    fig.update_layout(height=600, width=1000, title_text="Date Vs Recorded Cases of {}".format(country),template="plotly_dark")
    fig.show()
country_visualization(grouped_data,'Brazil')
