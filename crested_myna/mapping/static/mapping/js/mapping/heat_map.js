export function createHeatmapLayer(data, map_element) {

    // Convert data to heatmap format: [latitude, longitude, intensity]
    const heatmapData = data.map(point => [point[0], point[1], 1]);

    // Create the heat layer
    const heatLayer = L.heatLayer(heatmapData, {
        radius: 20,    // Adjust the radius to control the spread
        blur: 10,      // Blur level
        maxZoom: 18,   // Max zoom level for the heat effect
        max: 1.0,       // Maximum intensity
        gradient: {
          1.0: '#9a0202ff', // darkest tone
          0.8: '#fd0505ff', 
          0.5: '#ff5e07ff',
          0.3: '#f67402ff',
          0.1: '#fa9140ff', // lightest tone
        }
    });

    // Add to map
    return heatLayer;
}
