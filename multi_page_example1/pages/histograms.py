import dash

dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np
import dash_mantine_components as dmc
from datetime import datetime

np.random.seed(2020)

layout = html.Div(
    [
        dmc.Button("Notify 1", id="button-1"),
        dmc.Button("Notify 2", id="button-2"),
        dcc.Graph(id="histograms-graph"),
        html.P("Mean:"),
        dcc.Slider(
            id="histograms-mean", min=-3, max=3, value=0, marks={-3: "-3", 3: "3"}
        ),
        html.P("Standard Deviation:"),
        dcc.Slider(id="histograms-std", min=1, max=3, value=1, marks={1: "1", 3: "3"}),
    ]
)


@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.histogram(data, nbins=30, range_x=[-10, 10])
    return fig


@callback(
    Output(
        "notifications-container",
        "children",
        allow_duplicate=True,
    ),
    Input("button-1", "n_clicks"),
    prevent_initial_call="initial_duplicate",
)
def load_data_1(n_clicks):
    print("load_data_1")
    if n_clicks:
        return (
            dmc.Notification(
                title="Error",
                id=f"notification-1-{datetime.now().timestamp()}",
                action="show",
                color="red",
                loading=False,
                message=f"Error loading part 1",
                autoClose=False,
            ),
        )
    return None


@callback(
    Output(
        "notifications-container",
        "children",
        allow_duplicate=True,
    ),
    Input("button-2", "n_clicks"),
    prevent_initial_call="initial_duplicate",
)
def load_data_2(n_clicks):
    print("load_data_2")
    if n_clicks:
        return (
            dmc.Notification(
                title="Success",
                id=f"notification-2-{datetime.now().timestamp()}",
                action="show",
                color="green",
                loading=False,
                message=f"Success loading part 2",
                autoClose=False,
            ),
        )
    return None
