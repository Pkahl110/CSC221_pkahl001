import pandas as pd
import plotly.express as px

# Manually create a DataFrame with NVIDIA stock price data
data = {
    'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07'],
    'Close': [239.91, 244.93, 242.56, 241.07, 239.32]
    # Add more dates and corresponding closing prices as needed
}

nvidia = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
nvidia['Date'] = pd.to_datetime(nvidia['Date'])

# Create a line plot of the closing price over time
fig = px.line(nvidia, x='Date', y='Close', title='NVIDIA Stock Price (2020)')

# Update the layout for better visualization
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Closing Price (USD)',
)

# Show the plot
fig.show()