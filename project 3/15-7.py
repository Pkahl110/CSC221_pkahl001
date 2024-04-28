import plotly.graph_objects as go
from plotly.subplots import make_subplots

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(3, max_result+1))
fig = go.Figure(data=[go.Bar(x=x_values, y=frequencies)])
fig.update_layout(
    title='Results of rolling three D6 dice 1,000,000 times',
    xaxis=dict(title='Result', dtick=1),
    yaxis=dict(title='Frequency of Result')
)
fig.show()