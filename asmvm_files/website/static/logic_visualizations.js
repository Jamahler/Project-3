var svgWidth = 1000;
var svgHeight = 500;

// create an SVG element
var svg = d3.select("#svg-area")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);



// Load csv data
d3.csv("../static/wine_ratings.csv").then(function(wineData) {

    console.log(wineData);

  
    // log a list of names
    var price = wineData.map(data => data.price);
    var points =  wineData.map(data => data.points);
    var variety =  wineData.map(data => data.variety);
    var province =  wineData.map(data => data.province);
    var location = wineData.map(data => data.location);
    var description = wineData.map(data => data.description);
    var winery = wineData.map(data => data.winery);
    console.log("price", price);
    console.log("rating", points);
    console.log("variety", variety);
    console.log("province", province);
    console.log("location", location);
    console.log("winery", winery);
    console.log("description", description);
    // Cast each hours value in wineData 
    wineData.forEach(function(data) {

    });
  }).catch(function(error) {
    console.log(error);
  });

  

// Create a map object
var myMap = L.map("map", {
  center: [41.1403, -100.7601],
  zoom: 5
});
// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);
// Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
for (var i = 0; i < wineData.length; i++) {
  var winery = wineData[i];
  L.marker(winery.location)
    .bindPopup("<h1>" + winery.winery + "</h1>")
    .addTo(myMap);}