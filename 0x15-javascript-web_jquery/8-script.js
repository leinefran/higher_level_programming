/* a Javascript script that fetches and lists all movies title
   by using this URL: https://swapi.co/api/films/?format=json

   All movie titles must be list in the HTML tag UL#list_movies
   You can’t use document.querySelector to select the HTML tag
   You must use the jQuery API */

$.get('https://swapi.co/api/films/?format=json', function( data ) {
  for (let result of data.results) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  }
});
