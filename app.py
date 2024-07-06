import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, abort
import json
import os

app = Flask(__name__)
# Read Mapbox access token from environment variable
MAPBOX_ACCESS_TOKEN = os.getenv('MAPBOX_ACCESS_TOKEN')

@app.route('/')
def index():
    return render_template('index.html', mapbox_access_token=MAPBOX_ACCESS_TOKEN)

# Load volcano data
with open('data/volcanoes.json') as f:
    volcanoes = json.load(f)['volcanoes']

def fetch_volcano_images(volcano_name):
    """
    Fetches the list of image URLs for a given volcano.

    Args:
        volcano_name (str): The name of the volcano.

    Returns:
        list: A list of image URLs.
    """
    image_base_url = f'http://149.165.154.65/data/HDF5EOS/precip_products/{volcano_name}/'
    images = []

    try:
        response = requests.get(image_base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        images = [image_base_url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith( '.png')]
    except requests.RequestException as e:
        print(f"Error fetching images for {volcano_name}: {e}")
    return images

@app.route('/volcano/<int:volcano_id>')
def volcano_detail(volcano_id):
    # Simulate data retrieval based on volcano_id (replace with actual logic)
    volcano = next((v for v in volcanoes if v['id'] == volcano_id), None)
    if not volcano:
        abort(404, description="Volcano not found")

    # Fetch the images using the helper function
    images = fetch_volcano_images(volcano['name'])

    return render_template('volcano.html', volcano=volcano, images=images)

@app.route('/api/volcanoes')
def get_volcanoes():
    return jsonify(volcanoes)

if __name__ == '__main__':
    app.run(debug=True)
