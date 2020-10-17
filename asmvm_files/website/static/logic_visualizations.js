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
    // Cast each hours value in tvData as a number using the unary + operator
    wineData.forEach(function(data) {

    });
  }).catch(function(error) {
    console.log(error);
  });
  
