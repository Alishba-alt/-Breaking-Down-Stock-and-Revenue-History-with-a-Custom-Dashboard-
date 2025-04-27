import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample DataFrame
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [8000, 8500, 7800, 8200, 8000],
    'Revenue': [50000, 52000, 48000, 51000, 50000],
    'Profit': [10000, 12000, 9000, 11000, 10000]
}
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Dynamic Statistics Dashboard"

# Layout of the Dash application
app.layout = html.Div(children=[
    html.H1("Dynamic Statistics Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting statistics
    html.Div([
        html.Label("Select Statistic:", style={'fontSize': 14}),
        dcc.Dropdown(
            id='statistics-dropdown',
            options=[
                {'label': 'Sales', 'value': 'Sales'},
                {'label': 'Revenue', 'value': 'Revenue'},
                {'label': 'Profit', 'value': 'Profit'}
            ],
            value='Sales',
            style={'width': '70%'}
        )
    ], style={'margin': '20px auto', 'textAlign': 'center'}),
    
    # Input container
    html.Div(
        id='input-container',
        className='input-container',
        style={'margin': '20px auto', 'padding': '10px', 'border': '1px solid #ddd', 'width': '70%', 'textAlign': 'center'}
    ),
    
    # Output container
    html.Div(
        id='output-container',
        className='output-container',
        style={'margin': '20px auto', 'padding': '10px', 'border': '1px solid #ddd', 'width': '70%', 'textAlign': 'center'}
    ),
])

# Callback function to update input and output containers
@app.callback(
    [Output('input-container', 'children'),
     Output('output-container', 'children')],
    [Input('statistics-dropdown', 'value')]
)
def update_containers(selected_statistic):
    # Update input container text
    input_text = f"Input for selected statistic: {selected_statistic}"
    
    # Generate output based on selected statistic
    if selected_statistic == 'Sales':
        output_text = f"Total Sales: {df[selected_statistic].sum()} units"
    elif selected_statistic == 'Revenue':
        output_text = f"Total Revenue: ${df[selected_statistic].sum():,.2f}"
    elif selected_statistic == 'Profit':
        output_text = f"Total Profit: ${df[selected_statistic].sum():,.2f}"
    else:
        output_text = "No statistic selected."

    return input_text, output_text

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)