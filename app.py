from flask import Flask, render_template, jsonify, abort
import json
import os

app = Flask(__name__)
# Read Mapbox access token from environment variable
MAPBOX_ACCESS_TOKEN = os.getenv('MAPBOX_ACCESS_TOKEN')
PLOT_BASE_URL = 'http://149.165.154.65/data/HDF5EOS/precip_products/precip_plots/'

@app.route('/')
def index():
    return render_template('index.html', mapbox_access_token=MAPBOX_ACCESS_TOKEN)

# Load volcano data
with open('data/volcanoes.json') as f:
    volcanoes = json.load(f)['volcanoes']

def fetch_volcano_plots(volcano_id):
    base_url = f'{PLOT_BASE_URL}/{volcano_id}/'
    rows =[
        {'Map': f'{base_url}{volcano_id}_map.png',
         'Annual': f'{base_url}{volcano_id}_annual.png'},
        {'Strength': f'{base_url}{volcano_id}_strength.png',
        'Bar': f'{base_url}{volcano_id}_bar.png'}
    ]
    return rows

@app.route('/volcano/<int:volcano_id>')
def volcano_detail(volcano_id):
    # Simulate data retrieval based on volcano_id (replace with actual logic)
    volcano = next((v for v in volcanoes if v['id'] == volcano_id), None)
    if not volcano:
        abort(404, description="Volcano not found")

    # Fetch the plots using the helper function
    rows = fetch_volcano_plots(volcano['id'])

    return render_template('volcano.html', volcano=volcano, rows=rows)

@app.route('/api/volcanoes')
def get_volcanoes():
    return jsonify(volcanoes)

@app.route('/volcanoes')
def volcanoes_list():
    # Assuming `get_volcanoes` is a function that retrieves all volcano data

    return render_template('volcanoes_list.html', volcanoes=volcanoes)

if __name__ == '__main__':
    app.run(debug=True)
