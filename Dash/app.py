import sys
import os
from dash import Dash, dcc, html, dash_table, Input, Output
import base64
import pandas as pd
from modules.animal_shelter import animalShelter

# Import the map from external file
from geolocation.geolocation import create_map

# Ensure module path is correct
module_path = os.path.dirname(os.path.abspath('/users/koimon/desktop/CRUD-MODULE-MAIN/CRUD-Module-main/animal_shelter.py'))
sys.path.insert(0, module_path)

# Credentials (unused in mock mode)
username = "admin"
password = "admin"
collection = 'breeds'
database = "humanitarian_services"
port = 27017
host = '127.0.0.1'

# Load CSV instead of DB
df = pd.read_csv('data/data.csv')

# Initialize DB in mock mode
db = animalShelter(username, password, host, database, collection, port, use_db=False)
db._connect()

app = Dash(__name__)

# Load logo if it exists; avoid crashing in containerized or minimal environments.
image_filename = 'assets/Logo.png'
if os.path.exists(image_filename):
    with open(image_filename, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
else:
    encoded_image = None

# Colors
COLORS = {
    "bg": "#f5f7fa",
    "card": "#ffffff",
    "accent": "#B30000",
    "accent_light": "#FF4D4D",
    "text": "#1a1a1a",
    "header": "#dfe6f9",
    "purple": "#7A5CFA",
    "blue": "#4DA3FF",
    "grey": "#e0e0e0"
}

# expose COLORS on app so callbacks can use app.COLORS
app.COLORS = COLORS

# Get map figure from external file
fig = create_map()

# Layout
app.layout = html.Div(style={"backgroundColor": COLORS["bg"], "minHeight": "100vh"}, children=[

    # HEADER BAR
    html.Div(
        style={
            "backgroundColor": COLORS["header"],
            "padding": "20px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "color": COLORS["text"],
            "boxShadow": "0px 2px 6px rgba(0,0,0,0.4)"
        },
        children=[
            html.Div([
                html.H1("Emergency Rescue Animal Services", style={"margin": "0", "fontSize": "28px"}),
                html.P("Humanitarian Missions For Missing Persons", style={"margin": "0", "opacity": "0.8"})
            ]),
            html.Img(src=f"data:image/png;base64,{encoded_image}", style={"height": "60px"}) if encoded_image else html.Div()
        ]
    ),

    # MAIN CONTENT WRAPPER
    html.Div(style={"padding": "30px"}, children=[

        # SEARCH BAR
        html.Div(
            style={
                "backgroundColor": COLORS["card"],
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 2px 8px rgba(0,0,0,0.5)",
                "marginBottom": "25px"
            },
            children=[
                html.H3("Search Animals", style={"color": COLORS["text"]}),
                dcc.Input(
                    id="search-box",
                    type="text",
                    placeholder="He's on the roof...",
                    style={
                        "width": "60%",
                        "padding": "10px",
                        "borderRadius": "8px",
                        "border": "1px solid #333",
                        "backgroundColor": "#ffffff",
                        "color": COLORS["text"],
                        "marginTop": "10px"
                    }
                )
            ]
        ),

        # TABLE + MAP SIDE-BY-SIDE
        html.Div(
            style={
                "display": "flex",
                "gap": "25px",
                "flexWrap": "wrap",
                "justifyContent": "space-between",
                "alignItems": "flex-start",
                "backgroundColor": COLORS["card"],
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 2px 8px rgba(0,0,0,0.5)"
            },
            children=[

                # LEFT SIDE — DATA TABLE
                html.Div(
                    style={"flex": "1 1 55%", "minWidth": "350px"},
                    children=[
                        html.H3(
                            "Search animals for your next person found",
                            style={"color": COLORS["text"], "marginTop": "0px"}
                        ),
                        dash_table.DataTable(
                            id='datatable-id',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict('records'),
                            editable=False,
                            filter_action='none',
                            sort_action='none',
                            page_action='native',
                            page_current=0,
                            page_size=6,
                            style_table={"width": "100%", "overflowX": "auto"},
                            style_header={
                                "backgroundColor": COLORS["accent"],
                                "color": "white",
                                "fontWeight": "bold",
                                "fontSize": "15px"
                            },
                            style_cell={
                                "whiteSpace": "normal",
                                "height": "auto",
                                "textAlign": "left",
                                "padding": "8px",
                                "fontSize": "14px",
                                "color": COLORS["text"],
                                "backgroundColor": COLORS["card"]
                            }
                        )
                    ]
                ),

                # RIGHT SIDE — MAP
                html.Div(
                    style={"flex": "1 1 40%","minWidth": "350px","padding": "10px","backgroundColor": 
                        COLORS["card"],"borderRadius": "12px"},
                    
                    children=[html.H3("Locations Of Dogs",style={"color": COLORS["text"], "marginTop": "0px"}),
                        dcc.Graph(id="map-graph",figure=fig,style={"height": "400px"},config={"scrollZoom": True}
                        )
                    ]
                )
            ]
        )
    ])
])

# --------------------------
# SEARCH + STYLE CALLBACKS
# --------------------------

@app.callback(
    Output("datatable-id", "data"),
    Input("search-box", "value")
)
def filter_table(search_value):
    if not search_value or search_value.strip() == "":
        return df.to_dict("records")

    query = search_value.lower()

    filtered = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains(query).any(),
        axis=1
    )]

    return filtered.to_dict("records")


@app.callback(
    Output("datatable-id", "style_data_conditional"),
    Input("datatable-id", "selected_columns")
)
def update_styles(selected_columns):
    if not selected_columns:
        return []
    return [{
        "if": {"column_id": col},
        "backgroundColor": app.COLORS["accent_light"],
        "color": "white"
    } for col in selected_columns]

# RUN APP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=False)
