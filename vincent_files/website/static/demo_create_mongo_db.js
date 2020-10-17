function showWines() {
  $.ajax({
    data: {
      wine: $("#wine-selector").val()
    },
    type: "POST",
    url: "/getwine",
    beforeSend: function() {
      $("#loading").show();
    },
    complete: function() {
      $("#loading").hide();
    }
  }).done(function(data) {

    for(var i=0 ; i<data.winesList.length; i++){

      $("#budget-dropdown").append(`<option value="${data.winesList[i]}"> ${data.winesList[i]} </option>");
    }

  });
}