# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data import countries_df
from builders import make_table

# import external stylesheet that reset the css and Google fonts.
stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily":"Open Sans, sans-serif",
    },
    children =[
        html.Header(
            style={"textAlign":"center", "paddingTop": "50px"},
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})],
        ),
        html.Div(
            style={"paddingTop": "50px"},
            children=[html.Div(children=[make_table(countries_df)])]),
    ],
)
if __name__ == '__main__':
    app.run_server(debug=True)