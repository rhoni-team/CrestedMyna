// country_polygons.js

export function styleCountries(feature) {
// style countries with a color based on the number of birds and if it is exotic or not
  return {
      fillColor: getColor(feature.properties.tot_birds_count, feature.properties.is_exotic),
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 1
  };
}

function getColor(tot_birds_count, is_exotic) {
    // if the country is not exotic, return a green color. Else, return a color based on the number of birds
    if (is_exotic === false) {
        return '#31a354';
    } else {
      return tot_birds_count > 20000  ? '#3f007d' :
           tot_birds_count > 10000  ? '#4a1486' :
           tot_birds_count > 5000   ? '#54278f' :
           tot_birds_count > 1000   ? '#756bb1' :
           tot_birds_count > 10   ? '#9e9ac8' :
           '#bcbddc';
    }
}
