import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sedan_Sales': [8000, 8500, 7800, 8200, 8000],
    'SUV_Sales': [7000, 7300, 7100, 7500, 7400],
    'Truck_Sales': [5000, 5200, 4800, 5100, 5050]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Vehicle Sales Analysis Dashboard"

# Layout of the Dash application
app.layout = html.Div(children=[
    html.H1("Vehicle Sales Trends Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='vehicle-type-dropdown',
        options=[
            {'label': 'Sedan', 'value': 'Sedan_Sales'},
            {'label': 'SUV', 'value': 'SUV_Sales'},
            {'label': 'Truck', 'value': 'Truck_Sales'}
        ],
        value='Sedan_Sales',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='sales-line-plot')
])

# Callback for interactivity
@app.callback(
    Output('sales-line-plot', 'figure'),
    [Input('vehicle-type-dropdown', 'value')]
)
def update_graph(selected_vehicle_type):
    fig = px.line(
        df,
        x='Year',
        y=selected_vehicle_type,
        title=f"{selected_vehicle_type.replace('_', ' ')} Trends Over Years",
        labels={'x': 'Year', 'y': 'Sales (Units)'}
    )
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)