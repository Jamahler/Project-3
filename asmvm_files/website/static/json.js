// $("#0").change(function() {

// 	var $dropdown = $(this);

// 	$.getJSON("/wines", filterFunction(data) {
	
// 		var key = $dropdown.val();
// 		var vals = [];
							
// 		switch(key) {
// 			case 'wines':
// 				vals = data.result.split(",");
// 				break;
// 		// 	// case 'snacks':
// 		// 	// 	vals = data.snacks.split(",");
// 		// 	// 	break;
// 		// 	// case 'base':
// 		// 	// 	vals = ['Please choose from above'];
// 		}
		
// 		var $secondChoice = $("#second-choice");
// 		$secondChoice.empty();
// 		$.each(vals, function(index, value) {
// 			$secondChoice.append("<option>" + value + "</option>");
// 		});

// 	});
// });


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



// $("#1").change(function() {

// 	var $dropdown = $(this);

// 	$.getJSON("jsondata/data.json", function(data) {
	
// 		var key = $dropdown.val();
// 		var vals = [];
							
// 		switch(key) {
// 			case 'beverages':
// 				vals = data.beverages.split(",");
// 				break;
// 			case 'snacks':
// 				vals = data.snacks.split(",");
// 				break;
// 			case 'base':
// 				vals = ['Please choose from above'];
// 		}
		
// 		var $secondChoice = $("#second-choice");
// 		$secondChoice.empty();
// 		$.each(vals, function(index, value) {
// 			$secondChoice.append("<option>" + value + "</option>");
// 		});

// 	});
// });

// $("#2").change(function() {

// 	var $dropdown = $(this);

// 	$.getJSON("jsondata/data.json", function(data) {
	
// 		var key = $dropdown.val();
// 		var vals = [];
							
// 		switch(key) {
// 			case 'beverages':
// 				vals = data.beverages.split(",");
// 				break;
// 			case 'snacks':
// 				vals = data.snacks.split(",");
// 				break;
// 			case 'base':
// 				vals = ['Please choose from above'];
// 		}
		
// 		var $secondChoice = $("#second-choice");
// 		$secondChoice.empty();
// 		$.each(vals, function(index, value) {
// 			$secondChoice.append("<option>" + value + "</option>");
// 		});

// 	});
// });