import sys
import os
# Path to the virtual environment
venv_path = '/var/www/Precip_web/web_env/'
site_packages = os.path.join(venv_path, 'lib/python3.10/site-packages')  # Replace python3.x with your Python version
sys.path.insert(0, site_packages)

# Add the Flask app directory to the Python path
sys.path.insert(0, '/var/www/Precip_web/')
from precip_web import app
application = app
