import plotly.graph_objects as go

def create_map():
    lat = [
        "34.05223","36.77826","40.71278","41.87811","29.76043",
        "39.73924","33.44838","47.60621","32.71574","37.77493",
        "44.42800","25.76168","45.51523","35.22709","42.36008",
        "36.16266","43.03890","30.33218","33.74900","27.95057",
        "40.76078","38.62700","39.95258","32.77666","36.16994"
    ]

    lon = [
        "-118.24368","-119.41793","-74.00594","-87.62980","-95.36980",
        "-104.99025","-112.07404","-122.33207","-117.16109","-122.41942",
        "-110.58850","-80.19179","-122.67840","-80.84313","-71.05888",
        "-86.78160","-87.90647","-81.65565","-84.38800","-82.45718",
        "-111.89105","-90.19940","-75.16522","-96.79699","-115.13983"
    ]

    text = [
        "Los Angeles Animal Services – North Central Shelter",
        "California Wildlife Center",
        "NYC Animal Care Centers – Manhattan",
        "PAWS Chicago Adoption Center",
        "Houston SPCA",
        "Dumb Friends League – Denver",
        "Phoenix Herpetological Sanctuary",
        "Seattle Humane",
        "San Diego Humane Society",
        "San Francisco SPCA – Mission Campus",

        "Yellowstone Wildlife Habitat",
        "Miami-Dade Animal Services",
        "Oregon Humane Society",
        "Carolina Raptor Center – Charlotte",
        "MSPCA Boston",
        "Nashville Humane Association",
        "Milwaukee County Zoo – Animal Rescue Program",
        "Jacksonville Humane Society",
        "Atlanta Humane Society",
        "Tampa Bay Wildlife Rescue",

        "Utah Wildlife Rehabilitation Center",
        "St. Louis Zoo – Wildlife Rescue",
        "Philadelphia Animal Care & Control",
        "Dallas Zoo – Wildlife Rehabilitation",
        "Las Vegas Animal Foundation"
    ]

    fig = go.Figure(go.Scattermapbox(lat=lat,lon=lon,text=text,mode="markers",marker=dict(size=9)))

    fig.update_layout(mapbox=dict(style="open-street-map",center=dict(lat=38.92, lon=-77.07),
        zoom=2,),
        height=400,
        margin=dict(l=0, r=0, t=0, b=0),
        hovermode="closest")

    return fig
