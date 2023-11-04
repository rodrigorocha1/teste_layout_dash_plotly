import dash_bootstrap_components as dbc
from dash import html, dcc
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

card = dbc.Card(
    dbc.Card(
        dbc.CardBody(
            [
                html.H5("Card title", className="card-title"),
                html.P(" but not much else"),
                dbc.Button("Go somewhere", color="primary"),
            ]
        )
    ),
)

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card)  
                for i in range(1, 5)
            ],
            className='card_teste',
        ),

        dbc.Row(
            html.Div(

                dcc.Graph(
                    figure=dict(
                        data=[
                            dict(
                                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                350, 430, 474, 526, 488, 537, 500, 439],
                                name='Rest of world',
                                marker=dict(
                                    color='rgb(55, 83, 109)'
                                )
                            ),
                            dict(
                                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                                299, 340, 403, 549, 499],
                                name='China',
                                marker=dict(
                                    color='rgb(26, 118, 255)'
                                )
                            )
                        ],
                        layout=dict(
                            title='US Export of Plastic Scrap',
                            showlegend=True,
                            legend=dict(
                                x=0,
                                y=1.0
                            ),
                            margin=dict(l=40, r=0, t=40, b=30)
                        )
                    ),
                    id='my-graph-example'
            ),
            className='segunda_div'

            )
            
            
        ),
        dbc.Row(
            html.Div(
                dcc.Graph(
                    figure=dict(
                        data=[dict(
                            x=[1, 2, 3, 4, 6, 7],
                            y=[3, 1, 2, 5, 7 , 8],
                            type='bar'
                        )]
                    )
                )
            )
        )
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)
