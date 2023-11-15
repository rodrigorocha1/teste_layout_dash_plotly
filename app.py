import dash_bootstrap_components as dbc
from dash import html, dcc
import dash
import plotly.graph_objects as go

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


valores = [i * 25 for i in range(1, 20)]


def gerar_tabela():
    table_header = [
        html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
    ]

    row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])

    table_body = [html.Tbody([row1 for i in range(1, 20)])]

    table = dbc.Table(table_header + table_body, bordered=True)

    return table


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

                ),
                dbc.Col(
                    html.Div(
                        'Columnm1',
                        style={'background': '#ff0000'},
                    ),
                    md=6,

                ),
            ]
        ),
        dbc.Row(
            html.Br()

        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        'Columnm1',
                        style={'background': '#ff0000'},
                    ),
                    lg=3
                ),
                dbc.Col(
                    html.Div(
                        'Columnm2', style={'background': '#0ff000'},
                    ),
                    lg=3,
                ),
                dbc.Col(
                    html.Div(
                        'Columnm3', style={'background': '#ff00ff'},
                    ),
                    lg=3,
                ),
                dbc.Col(
                    html.Div(
                        'Columnm3', style={'background': '#ff00ff'},
                    ),
                    lg=3,
                ),
            ],
        ),
        dbc.Row(
            html.Div(
                gerar_tabela(),
                id='id_div_pg',
                className='class_div_pg'
            ),
            id='id_quarta_linha',
            className='class_quarta_linha'
        ),
        dbc.Row(
            dcc.Graph(
                id='grafico-de-barras',


                figure={
                    'data': [
                        {'x': valores, 'y': [
                            f'Barras {i+1}' for i in range(len(valores))],
                            'type': 'bar',
                            'orientation': 'h',
                            'width': 0.9,
                            'bargap': 0.001,
                            'bargroupgap': 0.009
                         },
                    ],
                    'layout': {
                        'title': 'Gráfico de Barras Horizontais',
                        'yaxis': {'tickfont': {'size': 14}},
                        'margin': {'l': 150, 'r': 10, 't': 30, 'b': 50}

                    },

                },
                style={'height': '800px'}
            ), className='class_grafico',
            style={'height': '800px'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
