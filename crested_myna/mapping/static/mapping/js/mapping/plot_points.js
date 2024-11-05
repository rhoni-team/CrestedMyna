export function createMap(map_id, center, zoom=2) {
  const map = L.map(map_id).setView(center, zoom);
  return map
}

export function createMarkerGroup(map_element) {
  var markerGroup = L.layerGroup().addTo(map_element);
  return markerGroup
}

export function addTile(map_element) {
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map_element);
}


function createMarker(location, map_element, marker_group) {
      var recordMarker = L.circleMarker(location, {
        color: 'red',
        fillColor: '#f03',
        radius: 2
      })
    recordMarker.addTo(marker_group);
    recordMarker.addTo(map_element);
}

export function addRecordsMarkers(record, map_element, marker_group) {
    for (var i=0; i<record.length; i++) {
      createMarker(record[i], map_element, marker_group);
    }
  }
  
  export function removeMarkers(marker_group) {
    marker_group.clearLayers();
  }
