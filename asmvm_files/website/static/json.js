
var apidata;
console.log('hey, you are connected to the json-wines index')
d3.json('/json-wines').then(function (wines_json) {
    console.log(wines_json)
    apidata = wines_json;

    console.log(apidata[0]);
    console.log(apidata[0].alcohol)
    console.log(apidata[0].flavonoids)
    stuff = d3.select('#data')
        .append('div')
        .data(apidata)
        .enter()
        .append('p')
        .text(function(d){
            return d.alcohol
        })
});

