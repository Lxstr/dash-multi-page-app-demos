import dash

dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import dash_mantine_components as dmc
from datetime import datetime

df = px.data.medals_wide(indexed=True)

layout = html.Div(
    [
        dmc.Button("Notify 3", id="button-3"),
        html.P("Medals included:"),
        dcc.Checklist(
            id="heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.tolist(),
        ),
        dcc.Graph(id="heatmaps-graph"),
    ]
)


@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig


@callback(
    Output(
        "notifications-container",
        "children",
        allow_duplicate=True,
    ),
    Input("button-3", "n_clicks"),
    prevent_initial_call="initial_duplicate",
)
def load_data_2(n_clicks):
    print("load_data_3")
    if n_clicks:
        return (
            dmc.Notification(
                title="Success",
                id=f"notification-3-{datetime.now().timestamp()}",
                action="show",
                color="green",
                loading=False,
                message=f"Success loading part 3",
                autoClose=False,
            ),
        )
    return None
