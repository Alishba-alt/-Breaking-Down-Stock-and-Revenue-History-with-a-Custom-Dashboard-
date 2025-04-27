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
    'Truck_Sales': [5000, 5200, 4800, 5100, 5050],
    'Region': ['North', 'South', 'East', 'West', 'North']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Enhanced Vehicle Sales Dashboard"

# Layout of the Dash application
app.layout = html.Div(children=[
    html.H1("Vehicle Sales Trends Dashboard", style={'textAlign': 'center'}),
    
    # First Dropdown: Select Vehicle Type
    html.Div([
        html.Label("Select Vehicle Type:", style={'fontSize': 14}),
        dcc.Dropdown(
            id='vehicle-type-dropdown',
            options=[
                {'label': 'Sedan', 'value': 'Sedan_Sales'},
                {'label': 'SUV', 'value': 'SUV_Sales'},
                {'label': 'Truck', 'value': 'Truck_Sales'}
            ],
            value='Sedan_Sales',
            style={'width': '70%'}
        )
    ], style={'margin': '20px auto', 'textAlign': 'center'}),
    
    # Second Dropdown: Filter by Region
    html.Div([
        html.Label("Filter by Region:", style={'fontSize': 14}),
        dcc.Dropdown(
            id='region-dropdown',
            options=[
                {'label': 'North', 'value': 'North'},
                {'label': 'South', 'value': 'South'},
                {'label': 'East', 'value': 'East'},
                {'label': 'West', 'value': 'West'}
            ],
            value='North',
            style={'width': '70%'}
        )
    ], style={'margin': '20px auto', 'textAlign': 'center'}),
    
    # Division for Output Display
    html.Div(
        id='output-display',
        className='output-container',
        style={'margin': '20px auto', 'padding': '10px', 'border': '1px solid #ddd', 'width': '70%', 'textAlign': 'center'}
    ),
    
    # Graph to Display Sales Trends
    dcc.Graph(id='sales-line-plot')
])

# Callback for interactivity
@app.callback(
    [Output('sales-line-plot', 'figure'),
     Output('output-display', 'children')],
    [Input('vehicle-type-dropdown', 'value'),
     Input('region-dropdown', 'value')]
)
def update_graph(selected_vehicle_type, selected_region):
    # Filter the DataFrame by region
    filtered_df = df[df['Region'] == selected_region]
    
    # Create the line plot
    fig = px.line(
        filtered_df,
        x='Year',
        y=selected_vehicle_type,
        title=f"{selected_vehicle_type.replace('_', ' ')} Trends in {selected_region}",
        labels={'x': 'Year', 'y': 'Sales (Units)'}
    )
    
    # Generate the output display text
    output_text = f"Displaying sales trends for {selected_vehicle_type.replace('_', ' ')} in the {selected_region} region."
    
    return fig, output_text

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)