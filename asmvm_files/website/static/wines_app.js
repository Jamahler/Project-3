function populateInput(id) {
    var input;
    var value;
    input = document.getElementById("myInput");
    value = document.getElementById(id);
    input.value = value.text;
  }
  function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
    var Parent = document.getElementById("table");
  while(Parent.hasChildNodes())
  {
     Parent.removeChild(Parent.firstChild);
  }
    let table = document.querySelector("table");
  if (input.value==('Red Wine')) {
  let data = Object.keys(recipes_for_red[0]);
  generateTable(table, recipes_for_red);
  }
  else if (input.value==('White Wine')) {
  let data = Object.keys(recipes_for_white[0]);
  generateTable(table, recipes_for_white);
  }
  else if (input.value==('Sparkling Wine')) {
  let data = Object.keys(recipes_for_sparkling[0]);
  generateTable(table, recipes_for_sparkling);
  }
  }
  let recipes_for_red = [
    { wine_type: document.getElementById('0').text, name: "Recipe 1", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('0').text, name: "Recipe 2", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('0').text, name: "Recipe 3", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('0').text, name: "Recipe 4", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('0').text, name: "Recipe 5", link_to_recipe:"google.com", image: "img.jpeg" },
  ];
  let recipes_for_white = [
    { wine_type: document.getElementById('1').text, name: "Recipe 1", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('1').text, name: "Recipe 2", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('1').text, name: "Recipe 3", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('1').text, name: "Recipe 4", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('1').text, name: "Recipe 5", link_to_recipe:"google.com", image: "img.jpeg" },
  ];
  let recipes_for_sparkling = [
  { wine_type: document.getElementById('2').text, name: "Recipe 1", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('2').text, name: "Recipe 2", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('2').text, name: "Recipe 3", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('2').text, name: "Recipe 4", link_to_recipe:"google.com", image: "img.jpeg" },
    { wine_type: document.getElementById('2').text, name: "Recipe 5", link_to_recipe:"google.com", image: "img.jpeg" },
  ];
  function generateTable(table, data) {
    for (let element of data) {
      let row = table.insertRow();
      for (key in element) {
        let cell = row.insertCell();
        let text = document.createTextNode(element[key]);
        cell.appendChild(text);
      }
    }
  }
  