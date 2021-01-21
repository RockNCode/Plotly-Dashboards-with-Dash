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
data = [go.Histogram(          # start with a normal scatter plot
    x=df['mpg'],
    xbins=dict(start=0,end=50,size=2)
)]
# create data by choosing fields for x, y and marker size attributes
layout = go.Layout(
    title='MPG',
    xaxis = dict(title = 'MPG'), # x-axis label
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='output.html')
