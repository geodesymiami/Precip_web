mapboxgl.accessToken = mapboxAccessToken;

// Initialize the Mapbox map
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/satellite-v9',
  center: [0, 0],
  zoom: 2,
  minZoom: 1,
  maxZoom: 18,
  maxBounds: [[-180, -85], [180, 85]] // Constrain the map to this area
});

// Create a single popup instance to reuse for hover
var hoverPopup = new mapboxgl.Popup({
  closeButton: false,
  closeOnClick: false
});

// Fetch volcano data from the API and add to the map
fetch('/api/volcanoes')
  .then(response => response.json())
  .then(data => {
    data.forEach(volcano => {
      // Create a marker for each volcano
      var marker = new mapboxgl.Marker()
        .setLngLat([volcano.longitude, volcano.latitude])
        .addTo(map);

      // Flag to track hover state
      let isHovered = false;

      // Add click event to redirect to volcano detail page
      marker.getElement().addEventListener('click', () => {
        window.location.href = `/volcano/${volcano.id}`;
      });

      // Add hover events to show the name of the volcano
      marker.getElement().addEventListener('mouseenter', () => {
        if (!isHovered) {
          hoverPopup
            .setLngLat([volcano.longitude, volcano.latitude])
            .setText(volcano.name)
            .addTo(map);
          isHovered = true;
        }
      });

      // Remove popup on mouse leave
      marker.getElement().addEventListener('mouseleave', () => {
        hoverPopup.remove();
        isHovered = false;
      });
    });
  })
  .catch(error => {
    console.error('Error fetching volcano data:', error);
  });

