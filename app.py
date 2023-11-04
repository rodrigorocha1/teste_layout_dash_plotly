import dash_bootstrap_components as dbc
from dash import html
import dash


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        'Columnm1', 
                        style={'background': '#ff0000'},
                    ),
                    md=6,
                    sm=4
                ),
                dbc.Col(
                    html.Div(
                        'Columnm2', style={'background': '#0ff000'}, 
                    ),
                    md=3,
                    sm=4,
                ),
                dbc.Col(
                    html.Div(
                        'Columnm3', style={'background':'#ff00ff'}, 
                    ),
                    md=3,
                    sm=4
                ),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
