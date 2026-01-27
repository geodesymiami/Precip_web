from flask import Flask, render_template, jsonify, abort
import json
import os
import sys

app = Flask(__name__)
# Read Mapbox access token from environment variable

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TOKEN_FILE = os.path.join(BASE_DIR, "mapbox_access_token.env")

def load_mapbox_token():
    if not os.path.exists(TOKEN_FILE):
        raise RuntimeError( f"MAPBOX token file missing: {TOKEN_FILE}")

    namespace = {}
    with open(TOKEN_FILE, "r") as f:
        exec(f.read(), namespace)
    token = namespace.get("mapbox_access_token", "").strip()

    if not token or "YourTokenHere" in token:
        raise RuntimeError( "MAPBOX access token not set (still placeholder)")

    return token

MAPBOX_ACCESS_TOKEN = load_mapbox_token()

PLOT_BASE_URL = 'http://149.165.155.152/data/precip_plots/'
PRECIP_WEB_HOME = os.getenv('PRECIP_WEB_HOME', os.path.dirname(__file__))

@app.route('/')
def index():
    return render_template('index.html', mapbox_access_token=MAPBOX_ACCESS_TOKEN)

# Load volcano data
with open(f'{PRECIP_WEB_HOME}/data/volcanoes.json') as f:
    volcanoes = json.load(f)['volcanoes']

def fetch_volcano_plots(volcano_id):
    base_url = f'{PLOT_BASE_URL}/{volcano_id}/'
    plots = {'Map': f'{base_url}{volcano_id}_map',
             'Annual': f'{base_url}{volcano_id}_annual',
             'Strength': f'{base_url}{volcano_id}_strength',
             'Bar': f'{base_url}{volcano_id}_bar'}
    return plots

@app.route('/volcano/<int:volcano_id>')
def volcano_detail(volcano_id):
    # Simulate data retrieval based on volcano_id (replace with actual logic)
    volcano = next((v for v in volcanoes if v['id'] == volcano_id), None)
    if not volcano:
        abort(404, description="Volcano not found")

    base_url = f'{PLOT_BASE_URL}{volcano_id}/{volcano_id}'

    return render_template('volcano.html', volcano=volcano, base_url=base_url)

@app.route('/api/volcanoes')
def get_volcanoes():
    return jsonify(volcanoes)

@app.route('/volcanoes')
def volcanoes_list():
    # Assuming `get_volcanoes` is a function that retrieves all volcano data

    return render_template('volcanoes_list.html', volcanoes=volcanoes)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
