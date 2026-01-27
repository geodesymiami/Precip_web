(minsar) //preceipvm2/var/www/Precip_web/precip_web[1191] ls
import sys
import os

# Add the Flask app directory to the Python path
# Note: The virtual environment is already activated by Apache's  WSGIDaemonProcess python-home directive,
# so we don't need to manually add site-packages or hardcode the Python version!
sys.path.insert(0, '/var/www/Precip_web/')

from precip_web import app
application = app
