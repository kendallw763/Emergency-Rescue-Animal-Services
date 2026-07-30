import sys
import os
from dash import Dash, dcc, html, Input, Output, dash_table
import base64
import pandas as pd
from modules.animal_shelter import animalShelter

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

# Initialize DB in mock mode so notebook runs without MongoDB
db = animalShelter(username, password, host, database, collection, port, use_db=False)
db._connect()   # Will skip connection

app = Dash(__name__)

# Load logo
image_filename = 'assets/Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode()

# --------------------------
# Dark Red / Off‑Black Theme
# --------------------------
COLORS = {
    "bg": "#0d0d0f",          # near-black background
    "card": "#1a1a1d",        # dark charcoal card
    "accent": "#B30000",      # deep bright red (matches your logo)
    "accent_light": "#CC0000",# slightly brighter red
    "text": "#e6e6e6",        # soft off-white text
    "header": "#0f0f11"       # slightly lighter black for header bar
}


app.layout = html.Div(style={"backgroundColor": COLORS["bg"], "minHeight": "100vh", "padding": "0px"}, children=[

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
            html.Img(
                src=f"data:image/png;base64,{encoded_image}",
                style={"height": "60px"}
            )
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
                        "backgroundColor": "#0f0f11",
                        "color": COLORS["text"],
                        "marginTop": "10px"
                    }
                )
            ]
        ),

        # TABLE ONLY (MAP REMOVED)
        html.Div(
            style={
                "backgroundColor": COLORS["card"],
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 2px 8px rgba(0,0,0,0.5)"
            },
            children=[
                html.H3("Search animals for your next person found", style={"color": COLORS["text"]}),
                dash_table.DataTable(
                    id='datatable-id',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    editable=False,
                    filter_action='none',     # remove built-in filter UI
                    sort_action='none',       # remove arrows
                    page_action='native',
                    page_current=0,
                    page_size=3,

                    style_table={
                        "width": "100%",
                        "overflowX": "auto"
                    },
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
        )
    ])
])

# --------------------------
# CALLBACKS
# --------------------------

# SEARCH FILTER
@app.callback(
    Output('datatable-id', 'data'),
    [Input('search-box', 'value')]
)
def filter_table(search_value):
    if not search_value:
        return df.to_dict('records')

    search_value = search_value.lower()

    filtered = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains(search_value).any(),
        axis=1
    )]

    return filtered.to_dict('records')

# COLUMN HIGHLIGHTING
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': COLORS["accent_light"],
        'color': 'white'
    } for i in selected_columns]


if __name__ == '__main__':
    app.run(debug=True)
