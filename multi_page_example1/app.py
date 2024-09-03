import dash
from dash import html, _dash_renderer
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

_dash_renderer._set_react_version("18.2.0")

app = dash.Dash(
    __name__,
    # Does not work
    # prevent_initial_callback="initial_duplicate",
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dmc.styles.NOTIFICATIONS],
)

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dmc.MantineProvider(
    children=[
        dmc.NotificationProvider(position="top-right", mt=180),
        html.Div(id="notifications-container"),
        dbc.Container(
            [navbar, dash.page_container],
            fluid=True,
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
