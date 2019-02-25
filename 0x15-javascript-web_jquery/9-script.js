/* a Javascript script that fetches and prints how to say “Hello”
   depending of the language.

   The translation of “Hello” must be display in the HTML tag DIV#hello
   You can’t use document.querySelector to select the HTML tag
   You must use the jQuery API
   You script must be work when it imported from the HEAD tag */

$.getJSON('https://fourtonfish.com/hellosalut/?lang=' + document.documentElement.lang, function (data) {
  $('DIV#hello').text(data.hello);
