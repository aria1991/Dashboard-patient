import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv("patient_data.csv")

# Create a line chart of heart rate over time
heart_rate_chart = px.line(df, x="time", y="heart_rate", title="Heart Rate Over Time")

# Create a scatterplot of blood pressure and pulse oximetry
bp_po_scatter = px.scatter(df, x="blood_pressure", y="pulse_oximetry", title="Blood Pressure vs. Pulse Oximetry")

# Create a bar chart of respiratory rate over time
respiratory_rate_bar = px.bar(df, x="time", y="respiratory_rate", title="Respiratory Rate Over Time")

# Create a line chart of temperature over time
temperature_line = px.line(df, x="time", y="temperature", title="Temperature Over Time")

# Create a Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(figure=heart_rate_chart),
    dcc.Graph(figure=bp_po_scatter),
    dcc.Graph(figure=respiratory_rate_bar),
    dcc.Graph(figure=temperature_line)
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
