$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (body) {
  const films = body.results;
  films.forEach(function (film) {
    $('#list_movies').append(`<li>${film.title}</li>`);
  });
});
