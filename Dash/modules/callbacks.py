import sys
import os
import app
from dash import Input, Output
import pandas as pd
from modules.animal_shelter import animalShelter


# --------------------------
# CALLBACKS - SEARCH FILTER
# --------------------------
df = pd.read_csv('data/data.csv')


COLORS = {
    "bg": "#0d0d0f",          # near-black background
    "card": "#1a1a1d",        # dark charcoal card
    "accent": "#B30000",      # deep bright red (matches your logo)
    "accent_light": "#CC0000",# slightly brighter red
    "text": "#e6e6e6",        # soft off-white text
    "header": "#0f0f11"       # slightly lighter black for header bar
}

class Callbacks:
    def __init__(self, app):
        self.app = app
        self.df = pd.read_csv('data/data.csv')
        self.register_callbacks()

    def register_callbacks(self):
        @self.app.callback(
            Output('datatable-id', 'data'),
            [Input('search-box', 'value')]
        )
        def filter_table(search_value):
            if not search_value:
                return self.df.to_dict('records')

            search_value = search_value.lower()

            filtered = self.df[self.df.apply(
                lambda row: row.astype(str).str.lower().str.contains(search_value).any(),
                axis=1
            )]

            return filtered.to_dict('records')

        @self.app.callback(
            Output('datatable-id', 'style_data_conditional'),
            [Input('datatable-id', 'selected_columns')]
        )
        def update_styles(selected_columns):
            return [{
                'if': {'column_id': i},
                'background_color': app.COLORS["accent_light"],
                'color': 'white'
            } for i in selected_columns]


