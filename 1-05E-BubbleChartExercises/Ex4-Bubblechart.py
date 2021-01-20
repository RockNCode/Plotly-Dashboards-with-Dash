#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# create a DataFrame from the .csv file:

df = pd.read_csv("../data/mpg.csv")
print(df)
data = [go.Scatter(          # start with a normal scatter plot
    x=df['weight'],
    y=df['horsepower'],
    text=df['name'],
    mode='markers',
    marker=dict(size=df['weight']/100) # set the marker size
)]
# create data by choosing fields for x, y and marker size attributes
layout = go.Layout(
    title='horsepower vs. weight',
    xaxis = dict(title = 'weight'), # x-axis label
    yaxis = dict(title = 'horsepower'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='output.html')







# create a layout with a title and axis labels







# create a fig from data & layout, and plot the fig
