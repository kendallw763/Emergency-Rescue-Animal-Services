import sys
import os
from dash import Dash, dcc, html, dash_table, Input, Output
import base64
import pandas as pd
from modules.animal_shelter import animalShelter

# Import the map from external file
from geolocation import create_map

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

# Load logo
image_filename = 'assets/Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode()

# Colors
COLORS = {
    "bg": "#f5f7fa",          # soft white/grey background
    "card": "#ffffff",        # pure white cards for clean contrast
    "accent": "#B30000",      # your logo red (kept exact)
    "accent_light": "#FF4D4D",# lighter red highlight
    "text": "#1a1a1a",        # deep grey/black text for readability
    "header": "#dfe6f9",      # light blue header (map‑matching)
    "purple": "#7A5CFA",      # soft purple accent (map‑matching)
    "blue": "#4DA3FF",        # light blue accent (map‑matching)
    "grey": "#e0e0e0"         # neutral grey for borders/dividers
}


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
                html.P("Humanitary Missions For Missing Persons", style={"margin": "0", "opacity": "0.8"})
            ]),
            html.Img(src=f"data:image/png;base64,{encoded_image}", style={"height": "60px"})
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
                    style={
                        "flex": "1 1 40%",
                        "minWidth": "350px",
                        "padding": "10px",
                        "backgroundColor": COLORS["card"],
                        "borderRadius": "12px"
                    },
                    children=[
                        html.H3(
                            "Locations Of Dogs",
                            style={"color": COLORS["text"], "marginTop": "0px"}
                        ),
                        dcc.Graph(
                            id="map-graph",
                            figure=fig,
                            style={"height": "400px"}
                        )
                    ]
                )
            ]
        )
    ])
])

# --- SEARCH CALLBACK ---
@app.callback(
    Output('datatable-id', 'data'),
    Input('search-box', 'value')
)
def update_table(search_value):
    """
    Filter the dataframe based on the search box text.
    Case-insensitive substring match across all columns.
    """

    if not search_value or search_value.strip() == "":
        return df.to_dict('records')

    query = search_value.lower()

    filtered = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains(query).any(),
        axis=1
    )]

    return filtered.to_dict('records')


# RUN APP
if __name__ == '__main__':
    app.run(debug=True)
