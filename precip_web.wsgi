import sys
import os

# Add the Flask app directory to the Python path
sys.path.insert(0, '/var/www/Precip_web/precip_web')

from precip_web import app

application = app()
