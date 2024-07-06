var map = L.map('map').setView([0, 0], 2); // Centered at [0, 0] with zoom level 2

// Add Mapbox Satellite tiles using the environment variable
L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    attribution: '© Mapbox © OpenStreetMap contributors',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

// Load volcano data from the API
fetch('/api/volcanoes')
    .then(response => response.json())
    .then(data => {
        data.forEach(volcano => {
            var marker = L.marker([volcano.latitude, volcano.longitude]).addTo(map);
            marker.bindTooltip(volcano.name, {
                permanent: false,  // Tooltip is shown on hover
                direction: 'top',  // Tooltip appears above the marker
                offset: [0, -10],  // Adjust tooltip position if necessary
            });
            marker.on('click', function() {
                window.location.href = `/volcano/${volcano.id}`;
            });
        });
    })
    .catch(error => {
        console.error('Error fetching volcano data:', error);
    });

// // Add logo to the map
// var logo = L.control({ position: 'topright' });
//
// logo.onAdd = function(map) {
//     var div = L.DomUtil.create('div', 'my-logo');
//     div.innerHTML = '<img src="/static/img/logo.png" alt="Logo" style="width: 100px; height: auto;">';
//     return div;
// };
//
// logo.addTo(map);
