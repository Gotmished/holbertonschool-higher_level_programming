$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (body) {
  $('#character').text(body.name);
});
