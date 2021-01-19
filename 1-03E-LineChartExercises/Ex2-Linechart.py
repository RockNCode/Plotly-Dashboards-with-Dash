#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
#df2 = df[[col for col in df.columns if col.startswith('DAY')]]


df2 = df[df['DAY']=='TUESDAY']
df2.set_index('LST_TIME', inplace=True)

print(df2.index)

data = []
# traces=[go.Scatter(
#     x = df2.columns,
#     y = df2.loc[name],
#     mode = 'markers+lines',
#     name = name
# ) for name in df2.index]
#
# layout = go.Layout(
#     title = 'Average temperature per day'
# )
#
# fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='output.html')
for day in days:
    # What should go inside this Scatter call?
    df_day = df[df['DAY']==day]
    df_day.set_index('LST_TIME', inplace=True)
    print(df_day[df_day['DAY']==day]['T_HR_AVG'])

    trace = go.Scatter(
        x = df_day.index,
        y = df_day[df_day['DAY']==day]['T_HR_AVG'],
        mode = 'markers+lines',
        name = day
    )
    data.append(trace)

# Define the layout


layout = go.Layout(
    title = 'AVG TEMP'
)


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='myout.html')
