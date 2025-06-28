
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('/home/enture/Downloads/dec_18_31/828ebf55-c802-49e6-b12e-1685a6aa3798_ampl_data.csv')
df.head()
df.columns
df.columns = ['param_id', 'workspace_name', 'base', 'param_name', 'epoch', 'timestamp', 'data']
df.head()
df['time'] = pd.to_datetime(df['timestamp'])

df.set_index('timestamp', inplace=True)
df.head()

sc = ['param_id', 'param_name', 'epoch','data']
df1 = df[sc]
df1.head()

df_extracted = df.pivot(index='time', columns='param_name', values='data')
df_extracted

df_extracted.loc[df_extracted['PF'].isnull(), 'PF'] = df_extracted['Active Power'] / df_extracted['Apparent Power']
df_e1 = df_extracted.fillna(method='bfill')
df_e1

df_e2 = df_e1.sort_index
df_e2

df_e1.isnull().sum().sum()

# weekly average consumption
df_e1['Weekday'] = df_e1.index.strftime('%A')

# Resample the data to weekly frequency and calculate the mean
df_weekly_avg = df_e1.resample('W').mean().round(2)

# Create a weekly bar chart using go.Figure
fig = go.Figure()

# Add bars for each power type
fig.add_trace(go.Bar(x=df_weekly_avg.index.week,
                     y=df_weekly_avg['Active Power'],
                     name='Active Power',
                     text=df_weekly_avg['Active Power'],  # Add data labels
                     textposition='auto'))  # Automatically place data labels

fig.add_trace(go.Bar(x=df_weekly_avg.index.week,
                     y=df_weekly_avg['Apparent Power'],
                     name='Apparent Power',
                     text=df_weekly_avg['Apparent Power'],  # Add data labels
                     textposition='auto'))  # Automatically place data labels

fig.add_trace(go.Bar(x=df_weekly_avg.index.week,
                     y=df_weekly_avg['Reactive Power'],
                     name='Reactive Power',
                     text=df_weekly_avg['Reactive Power'],  # Add data labels
                     textposition='auto'))  # Automatically place data labels

fig.add_trace(go.Bar(x=df_weekly_avg.index.week,
                     y=df_weekly_avg['PF'],
                     name='PF',
                     text=df_weekly_avg['PF'],  # Add data labels
                     textposition='auto'))  # Automatically place data labels

# Define date ranges for each week
date_ranges = [f"Week: {start.strftime('%b %d, %Y')} to {end.strftime('%b %d, %Y')}"
               for start, end in zip(df_weekly_avg.index.to_period('W').start_time, df_weekly_avg.index.to_period('W').end_time)]

# Update layout
fig.update_layout(
    barmode='group',  # Use 'group' for grouped bars, 'stack' for stacked bars
    title='Weekly Average Power Consumption',
    xaxis=dict(title='Week', tickmode='array', tickvals=df_weekly_avg.index.week.unique(), ticktext=date_ranges),
    yaxis=dict(title='Values'),
    height=400
)

# Show the chart
fig.show()

# Total Active Power of Days of week like total sundays, mondays, tuesdays....

day_counts = df_e1.groupby(df_e1.index.day_name())['Active Power'].sum().round(2)

# Create a pie chart using Plotly Express
fig = px.pie(names=day_counts.index, values=day_counts.values, hole=0.4, title='Total Active Power by Days of the Week')

# Add data labels
fig.update_traces(textinfo='value+percent+label')

# Update layout with smaller figsize
fig.update_layout(
    width=900,  # Set the width to your desired value
    height=400   # Set the height to your desired value
)

# Show the chart
fig.show()

# Total days of week in dognut chart for PF 
day_counts = df_e1.groupby(df_e1.index.day_name())['PF'].sum()
day_counts = day_counts.round(2)
fig = px.pie(names=day_counts.index, values=day_counts.values, hole=0.4, title='Total PF by Days of the Week')

fig.update_traces(textinfo='value+percent+label')

fig.show()

# total Apparent Power of days of week in dognut chart
day_counts = df_e1.groupby(df_e1.index.day_name())['Apparent Power'].sum().round(2)

# Create a pie chart using Plotly Express
fig = px.pie(names=day_counts.index, values=day_counts.values, hole=0.4, title='Total Apparent Power by Days of the Week')

# Add data labels
fig.update_traces(textinfo='value+percent+label')

# Update layout with smaller figsize
fig.update_layout(
    width=1000,  # Set the width to your desired value
    height=500   # Set the height to your desired value
)

# Show the chart
fig.show()

# total Active power overall
day_counts = df_e1.groupby(df_e1.index.day_name())['Active Power'].sum().round(2)

# Create a Gauge chart using go.Figure
fig = go.Figure()

# Add a Gauge trace
fig.add_trace(go.Indicator(
    mode='gauge+number',
    value=day_counts.sum(),  # Total Active Power
    title={'text': 'Total Active Power'},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [None, day_counts.sum()]},
        'bar': {'color': 'darkblue'},
        'steps': [
            {'range': [0, day_counts.sum()], 'color': 'lightblue'}
        ],
        'threshold': {
            'line': {'color': 'red', 'width': 2},
            'thickness': 0.75,
            'value': day_counts.sum()
        }
    }
))

# Update layout with smaller figsize
fig.update_layout(
    title='Total Active Power by days of the month',
    height=300,  # Set the height to your desired value
    width=400    # Set the width to your desired value
)

# Show the chart
fig.show()

# Total Apparent power of overall 

day_counts = df_e1.groupby(df_e1.index.day_name())['Apparent Power'].sum().round(2)

# Create a Gauge chart using go.Figure
fig = go.Figure()

# Add a Gauge trace
fig.add_trace(go.Indicator(
    mode='gauge+number',
    value=day_counts.sum(),  # Total Apparent Power
    title={'text': 'Total Apparent Power'},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [None, day_counts.sum()]},
        'bar': {'color': 'darkblue'},
        'steps': [
            {'range': [0, day_counts.sum()], 'color': 'lightblue'}
        ],
        'threshold': {
            'line': {'color': 'red', 'width': 2},
            'thickness': 0.75,
            'value': day_counts.sum()
        }
    }
))

# Update layout with smaller figsize
fig.update_layout(
    title='Total Apparent Power by Days of the month',
    height=300,  # Set the height to your desired value
    width=400    # Set the width to your desired value
)

# Show the chart
fig.show()

#total PF of overall 

day_counts = df_e1.groupby(df_e1.index.day_name())['PF'].sum().round(2)

# Create a Gauge chart using go.Figure
fig = go.Figure()

# Add a Gauge trace
fig.add_trace(go.Indicator(
    mode='gauge+number',
    value=day_counts.sum(),  # Total PF
    title={'text': 'Total PF'},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [None, day_counts.sum()]},
        'bar': {'color': 'darkblue'},
        'steps': [
            {'range': [0, day_counts.sum()], 'color': 'lightblue'}
        ],
        'threshold': {
            'line': {'color': 'red', 'width': 2},
            'thickness': 0.75,
            'value': day_counts.sum()
        }
    }
))

# Update layout with smaller figsize
fig.update_layout(
    title='Total PF by Days of the month',
    height=300,  # Set the height to your desired value
    width=400    # Set the width to your desired value
)

# Show the chart
fig.show()