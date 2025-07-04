import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
from datetime import datetime
from pytz import timezone

df1 = pd.read_csv('dec_2023.csv')
df2 = pd.read_csv('TableData.csv')
 
# Merge DataFrames on 'param_id' with left join
df = pd.merge(df1, df2, on='param_id', how='left')
df.head()

df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_convert('Asia/Kolkata')
df.set_index('timestamp', inplace=True)

selected_columns = ['param_id', 'organisation_id', 'data', 'workspace_name', 'device_name', 'name']
df_sc = df[selected_columns]
df_sc.head()

selected_columns = ['param_id', 'organisation_id', 'data', 'workspace_name', 'device_name', 'name']
df_sc = df[selected_columns]
# Sort the DataFrame by timestamp
df_sc_sorted = df_sc.sort_index()
# Display the sorted DataFrame
print(df_sc_sorted.head())

df['workspace_name'].unique()

df['name'].unique()

df['device_name'].unique()

sdn = ['Ambient Sensor - Ground Floor', 'Trough Sensor- Ground Floor']
df_filtered = df_sc_sorted[df_sc_sorted['device_name'].isin(sdn)]
# Display the filtered DataFrame
print(df_filtered.head())

selected_devices = ['Ambient Sensor - Ground Floor', 'Trough Sensor- Ground Floor']
selected_names = ['Temperature', 'Humidity', 'Active Energy Consumption','Active Energy consumption' ]
df_filtered = df_sc_sorted[df_sc_sorted['device_name'].isin(selected_devices) & df_sc_sorted['name'].isin(selected_names)]

# Display the filtered DataFrame
print(df_filtered.head())

# Create a line chart using Plotly Express
fig = px.line(df_filtered, x=df_filtered.index, y='data', color='name', 
              facet_col='device_name', facet_col_wrap=1,
              labels={'data': 'Data', 'timestamp': 'Timestamp'}, 
              title='Ambient Sensor & Trough Sensor - Ground Floor Temperature and Humidity')

# Add data points to the line chart
fig.update_traces(mode='markers+lines', hovertemplate=None)

# Show the plot
fig.show()

selected_devices = ['Ambient Sensor- Top Floor', 'Trough Sensor-Top Floor']
selected_names = ['Temperature', 'Humidity', 'Active Energy Consumption','Active Energy consumption' ]
df_filtered_tf= df_sc_sorted[df_sc_sorted['device_name'].isin(selected_devices) & df_sc_sorted['name'].isin(selected_names)]

# Create a line chart using Plotly Express
fig = px.scatter(df_filtered_tf, x=df_filtered_tf.index, y='data', color='name', 
              facet_col='device_name', facet_col_wrap=1,
              labels={'data': 'Data', 'timestamp': 'Timestamp'}, 
              title='Ambient Sensor & Trough Sensor - Top Floor Temperature and Humidity')

line_fig = px.line(df_filtered_tf, x=df_filtered_tf.index, y='data', color='name')

# Add data points to the line chart
fig.update_traces(mode='markers+lines', hovertemplate=None)

# Show the plot
fig.show()

selected_devices = ['MOTOR 3']
selected_names = ['Temperature', 'Humidity', 'Active Energy Consumption', 'Active Energy consumption']
df_filtered = df_sc_sorted[df_sc_sorted['device_name'].isin(selected_devices) & df_sc_sorted['name'].isin(selected_names)]

# Create a scatter plot using Plotly Express
fig = px.scatter(df_filtered, x=df_filtered.index, y='data', color='name',
                 labels={'data': 'Data', 'timestamp': 'Timestamp'},
                 title='MOTOR 3 Active Energy Consumption - Scatter Plot')

# Create a line chart using Plotly Express
line_fig = px.line(df_filtered, x=df_filtered.index, y='data', color='name')

# Add scatter points to the line chart
for trace in line_fig.data:
    fig.add_trace(trace)

# Show the plot
fig.show()

selected_devices = ['MOTOR 3', 'MOTOR 1', 'MOTOR 2 ', 'MOTOR 2']
selected_names = ['Active Energy Consumption']
df_filtered_tf= df_sc_sorted[df_sc_sorted['device_name'].isin(selected_devices) & df_sc_sorted['name'].isin(selected_names)]

# Create a line chart using Plotly Express
fig = px.scatter(df_filtered_tf, x=df_filtered_tf.index, y='data', color='device_name', 
              labels={'data': 'Data', 'timestamp': 'Timestamp'}, 
              title='Ambient Sensor & Trough Sensor - Top Floor Temperature and Humidity')

line_fig = px.line(df_filtered_tf, x=df_filtered_tf.index, y='data', color='name')

# Add data points to the line chart
fig.update_traces(mode='markers+lines', hovertemplate=None)

# Show the plot
fig.show()

######################
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
from datetime import datetime
from pytz import timezone

df1 = pd.read_csv('hm_data_dec_2023.csv')
df2 = pd.read_csv('ModbusParamViewTableData.csv')
 
# Merge DataFrames on 'param_id' with left join
df = pd.merge(df1, df2, on='param_id', how='left')

df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_convert('Asia/Kolkata')
df.set_index('timestamp', inplace=True)

selected_columns = ['param_id', 'organisation_id', 'data', 'workspace_name', 'device_name', 'name']
df_sc = df[selected_columns]

# Sort the DataFrame by timestamp
df_sc_sorted = df_sc.sort_index()
df_sc_sorted.head(5)

df['workspace_name'].unique()
array(["'Jumbo TroughT&H", "'Jumbo Trough 3", "'Jumbo Trough 1",
       "'Jumbo Trough 2", "'Jumbo Trough 4"], dtype=object)

df['device_name'].unique()
array(['Ambient Sensor- Top Floor', 'Trough Sensor-Top Floor',
       'Ambient Sensor - Ground Floor', 'Trough Sensor- Ground Floor',
       'MOTOR 3', 'MOTOR 1', 'MOTOR 2 ', 'MOTOR 2'], dtype=object)

df['name'].unique()
array(['Humidity', 'Temperature', 'Voltage L-L', 'Active Power',
       'Reactive Power', 'PF', 'Active Energy consumption',
       'Apparent Energy consumption', 'Current', 'Apparent Power',
       'Active Energy Consumption', 'Apparent Energy Consumption',
       'Current ', 'Apprent Power'], dtype=object)

M1 = df_sc_sorted[df_sc_sorted['device_name'] == 'MOTOR 1']
M2 = df_sc_sorted[df_sc_sorted['device_name'] == 'MOTOR 2']
M3 = df_sc_sorted[df_sc_sorted['device_name'] == 'MOTOR 3']

names_to_filter = ['Humidity', 'Temperature', 'Active Energy consumption', 'Active Energy Consumption']

M1_nf = M1[M1['name'].isin(names_to_filter)]   # nf = name filter
M2_nf = M2[M2['name'].isin(names_to_filter)]
M3_nf = M3[M3['name'].isin(names_to_filter)]

