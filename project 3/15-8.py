import plotly.graph_objects as go
from plotly.subplots import make_subplots

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(1, max_result+1))
fig = go.Figure(data=[go.Bar(x=x_values, y=frequencies)])

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
fig.update_layout(
    title='Results of multiplying two D6 dice (1,000,000 rolls)',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
fig.show()