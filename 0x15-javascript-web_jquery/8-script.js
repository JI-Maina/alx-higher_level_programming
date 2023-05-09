// fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $.each(data.results, function (index, movie) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });        
});
