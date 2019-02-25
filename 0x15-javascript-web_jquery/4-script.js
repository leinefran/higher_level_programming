/* a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:
 The HEADER tag must always have one class: red or green, never both in the same time, never empty.
 If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
 You can’t use document.querySelector to select the HTML tag
 You must use the jQuery API */

$('#toggle_header').on('click', function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
