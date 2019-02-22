/* a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
 You can’t use document.querySelector to select the HTML tag
 You must use the jQuery API */

$('#red_header').on('click', function () {
  $('header').addClass('red');
});
