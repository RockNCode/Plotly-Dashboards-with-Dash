#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# create a data variable:
length = df['length']
#print(length)

data = [go.Histogram(
    x=length,
    xbins=dict(start=0,end=1,size=.02)
)]
# create a fig from data & layout, and plot the fig

layout = go.Layout(
    title='Length',
    xaxis = dict(title = 'Length'), # x-axis label
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='output.html')
