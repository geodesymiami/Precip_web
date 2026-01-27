# Rain rain go away
Flask based website to display precipitation plots from [geodesymiami/Precip](https://github.com/geodesymiami/precip).

## Installation
1. Go to `/var/www/` and clone the repository:
```
git clone git@github.com:geodesymiami/precip_web
```
2. Install the required packages into an virtual environment:
```bash
python -m venv web_env
source web_env/bin/activate
pip install -r requirements.txt
```
3. Make sure the MAPBOX_ACCESS_TOKEN is set in `mapbox_access_token.env`. If it exists it will use `~accounts/mapbox_access_token.env`.

5. Run the website
```
cd precip_web/
python run.py
```
6. Open Website at the given address (chrome/safari)
```
127.0.0.1:5000
```
or check using
```
curl -s http://127.0.0.1:5000
```
7. On a remote server, to configure Apache create `/etc/apache2/sites-available/precip_web.conf` containing
```
<VirtualHost *:80>

    # Alias directives must come BEFORE WSGIScriptAlias to prevent Flask from catching these URLs

    # Serve /data/HDF5EOS/ as static files (bypass WSGI/Flask)
    Alias /data/HDF5EOS/ /data/HDF5EOS/
    <Directory /data/HDF5EOS/>
        Options Indexes FollowSymLinks
        Require all granted
    </Directory>

    # Serve /data/precip_plots/ as static files
    Alias /data/precip_plots/ /data/precip_plots/
    <Directory /data/precip_plots/>
        Options Indexes FollowSymLinks
        Require all granted
    </Directory>

    # Flask/WSGI configuration (must come AFTER Alias directives)
    WSGIDaemonProcess precip_web python-home=/var/www/Precip_web/web_env python-path=/var/www/Precip_web
    WSGIProcessGroup precip_web
    WSGIScriptAlias / /var/www/Precip_web/web.wsgi

    <Directory /var/www/Precip_web/>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/precip_web_error.log
    CustomLog ${APACHE_LOG_DIR}/precip_web_access.log combined
</VirtualHost>
```
or
```
sudo cp precip_web.conf /etc/apache2/sites-available/
```
8. Start Apache using:
```
sudo a2ensite precip_web.conf
sudo systemctl restart apache2
```
8. Check for errors using:
```
sudo tail -20 /var/log/apache2/error.log
```
If you see a Traceback, then python could not properly run your `precip_web.wsgi` or `app.py`.



### TODOS:
- [x] Add a map to the website
- [x] Parse data from the [volcano list](https://github.com/geodesymiami/precip/blob/main/src/precip/Holocene_Volcanoes_precip_cfg..xlsx)
- [x] Run [geodesymiami/Precip](https://github.com/geodesymiami/precip) on Merapi, hosted on [jetstream](http://149.165.154.65/data/HDF5EOS/precip_products/Merapi/)
- [ ] Set up cron job to automatically run precip plots (0 0 1 * * run_plot_precipitation_all.py)
- [ ] fix title (mobile)
- [ ] remove automatic scaling
- [ ] add magnify icon for image hover
- [ ] add esc on image zoom to escape
- [ ] fix citations in about
- [ ] remove designed by kawan
- [ ] add no bin button

### WEB DESIGN TODOS:
- [x] Use Mapbox for satellite imagery map
- [x] Add UM GeodesyLab logo
- [x] Add a hover effect over points on the map
- [x] Add volcano metadata on <volcano id> page
- [x] Add a link to the volcano's smithsonian page
- [x] Add a separate page for the volcano list (by country)
- [ ] Add a search bar to search for volcanoes ?
- [ ] Indicate the last time the data was updated and plot was generated


