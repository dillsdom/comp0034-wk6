from dash import Dash, html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

row_one = dbc.Row([
    dbc.Col([html.H1("Paralympics Data Analytics"),
html.P(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce efficitur posuere metus posuere malesuada. ")]),
])

row_two = dbc.Row([
    dbc.Col(children=[dbc.Select(
    options=[
        {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events",  # The default selection
    id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
),], width=2),
    dbc.Col(children=[html.Img(src=app.get_asset_url('event-chart-placeholder.png'), className="img-fluid",width=4),]),
    dbc.Col(children=[html.Div(
    [
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],  # Values is a list as you can select 1 AND 2
            id="checklist-input",
        ),
    ]
)
], width={"size": 2, "offset": 4}), 
    dbc.Col(children=[html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid",width=4)]) # 4 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(children=[html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid")], width=6),
    dbc.Col(children=[dbc.Card(
    [
        dbc.CardImg(src="assets/logos/1960_Rome.png", top=True),
        dbc.CardBody(
            [
                html.H4("TownName 2026", className="card-title"),
                html.P(
                    "Highlights of the paralympic event will go here. This will be a sentence or two.",
                    className="card-text",
                ),
                html.P(
                    "Number of athletes: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of events: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of countries: XX",
                    className="card-text",
                ),
            ]
        ),
    ],
    # style={"width": "18rem"},
)], width=6),
])

row_four = dbc.Row([
    dbc.Col(children=[], width=6),
    dbc.Col(children=[], width=6),
])

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])
'''
app.layout = dbc.Container(html.Div([
        dbc.Row(dbc.Col(html.Div("Heading and intro"),width=12)),
        dbc.Row([dbc.Col(html.Div("2 cols:\n dropdown"),width=2),
                dbc.Col(html.Div(),width=4),
                dbc.Col(html.Div("2 cols, offset by 4 cols:\n checkbox"),width=2),
                dbc.Col(html.Div(),width=4)]),
        dbc.Row([dbc.Col(html.Div("6 cols: Line Chart"),width=6),
                dbc.Col(html.Div("6 cols: Bar Chart"),width=6)]),
        dbc.Row([dbc.Col(html.Div("6 cols: Map with event markers"),width=6),
                dbc.Col(html.Div("6 cols: card showing event info"),width=6)])
    ]))
                
'''
if __name__ == '__main__':
    app.run(debug=True, port=8060)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
