var map = L.map('map', {
    center: [0, 0],
    zoom: 2,
    zoomAnimation: true,
    zoomAnimationThreshold: 4,
    fadeAnimation: true,
    easeLinearity: 0.25,
    zoomSnap: 0.1,
    zoomDelta: 0.5,
    wheelPxPerZoomLevel: 60
});

// Add Mapbox Satellite tiles using the environment variable
L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    attribution: '© Mapbox © OpenStreetMap contributors',
    tileSize: 256, // Change tile size to 256
    zoomOffset: 0, // Adjust zoom offset for the new tile size
    updateWhenIdle: true,
    updateWhenZooming: false,
    maxNativeZoom: 19, // Adjust based on the level of detail needed
}).addTo(map);

// Load volcano data from the API
fetch('/api/volcanoes')
    .then(response => response.json())
    .then(data => {
        data.forEach(volcano => {
            var marker = L.marker([volcano.latitude, volcano.longitude]).addTo(map);
            marker.bindTooltip(volcano.name, {
                permanent: false,
                direction: 'top',
                offset: [0, -10],
            });
            marker.on('click', function() {
                window.location.href = `/volcano/${volcano.id}`;
            });
        });
    })
    .catch(error => {
        console.error('Error fetching volcano data:', error);
    });
