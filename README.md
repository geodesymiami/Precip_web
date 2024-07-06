# Rain rain go away
Flask based website to display precipitation plots from [geodesymiami/Precip](https://github.com/geodesymiami/precip).

## Installation
1. Clone the repository
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Make sure the MAPBOX_ACCESS_TOKEN is set in your environment variables
```bash
export MAPBOX_ACCESS_TOKEN=<your_mapbox_access_token>
```
4. Run the website
```bash
python run.py
```
5. Open Website at the given address (chrome/safari)
```127.0.0.1:5000
```

### TODOS:
- [x] Add a map to the website
- [x] Parse data from the [volcano list](https://github.com/geodesymiami/precip/blob/main/src/precip/Holocene_Volcanoes_precip_cfg..xlsx)
- [x] Run [geodesymiami/Precip](https://github.com/geodesymiami/precip) on Merapi, hosted on [jetstream](http://149.165.154.65/data/HDF5EOS/precip_products/Merapi/)
- [ ] Set up cron job to automatically run precip plots
- [ ] Make basic tests (pytest)
- [ ] Add an explanation on homepage

### WEB DESIGN TODOS:
- [x] Use Mapbox for satellite imagery map
- [x] Add UM GeodesyLab logo
- [x] Add a hover effect over points on the map
- [x] Add volcano metadata on <volcano id> page
- [ ] Add a link to the volcano's smithsonian page
- [ ] Add a separate page for the volcano list (by country)
- [ ] Add a search bar to search for volcanoes ?
- [ ] Indicate the last time the data was updated and plot was generated


