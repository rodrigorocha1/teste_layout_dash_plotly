import dash_bootstrap_components as dbc
from dash import html, dcc
import dash
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

n = 50  # Número de amostras
r = 40  # Razão

valores = [i * 25 for i in range(1, n)]


def gerar_tabela():
    table_header = [
        html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
    ]

    row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])

    table_body = [html.Tbody([row1 for i in range(1, 6)])]

    table = dbc.Table(table_header + table_body, bordered=True)

    return table


fig = px.bar(
    x=valores,
    y=[f'Barras {i}' for i in range(len(valores))],
    orientation='h',
    text=valores,  # Adicione os valores como texto dentro das barras
)

fig.update_layout(
    title='Gráfico de Barras Horizontais',
    yaxis=dict(tickfont=dict(size=15), automargin=True),
    margin=dict(l=150, r=10, t=30, b=50),
    # width=400,  # Defina a largura desejada
    height=(n * r)  # Defina a altura desejada
)

fig2 = px.bar(
    x=valores,
    y=[f'Barras {i}' for i in range(len(valores))],
    orientation='h',
    text=valores,  # Adicione os valores como texto dentro das barras
)

fig2.update_layout(
    title='Gráfico de Barras Horizontais',
    yaxis=dict(tickfont=dict(size=15), automargin=True),
    margin=dict(l=150, r=10, t=60, b=50),
    # width=400,  # Defina a largura desejada
    height=(n * r) - 30  # Defina a altura desejada
)


app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [

                        html.Div(
                            'Columnm1',
                            style={'background': '#ff0000'},
                        )
                    ],
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
            [

                dbc.Col(
                    [

                        dcc.Graph(
                            id='grafico-de-barras',
                            figure=fig,

                            # figure={
                            #     'data': [
                            #         {'x': valores, 'y': [
                            #             f'Barras {i} <br>' for i in range(len(valores))],
                            #             'type': 'bar',
                            #             'orientation': 'h',
                            #             'width': 0.9,
                            #             'bargap': 0.001,
                            #             'bargroupgap': 0.009
                            #          },
                            #     ],
                            #     'layout': {
                            #         'title': 'Gráfico de Barras Horizontais',
                            #         'yaxis': {'tickfont': {'size': 10}, 'automargin': True},
                            #         'margin': {'l': 150, 'r': 10, 't': 30, 'b': 50}

                            #     },

                            # },

                        ),
                    ],

                    md=6
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(dbc.Select(),), dbc.Col(dbc.Select(),),
                            ]
                        ),

                        dbc.Row(
                            [
                                dcc.Graph(
                                    id='grafico-de-barras_2',
                                    figure=fig2,

                                    # figure={
                                    #     'data': [
                                    #         {'x': valores, 'y': [
                                    #             f'Barras {i} <br>' for i in range(len(valores))],
                                    #             'type': 'bar',
                                    #             'orientation': 'h',
                                    #             'width': 0.9,
                                    #             'bargap': 0.001,
                                    #             'bargroupgap': 0.009
                                    #          },
                                    #     ],
                                    #     'layout': {
                                    #         'title': 'Gráfico de Barras Horizontais',
                                    #         'yaxis': {'tickfont': {'size': 10}, 'automargin': True},
                                    #         'margin': {'l': 150, 'r': 10, 't': 30, 'b': 50}

                                    #     },

                                    # },

                                )
                            ]
                        )
                    ],
                    md=6,
                    style={'height': f'{(n * r)}px'}
                ),
            ],
            className='class_grafico',
            style={'height': f'{(n * r) }px'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
