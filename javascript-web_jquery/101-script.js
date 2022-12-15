$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('ul.my_list').find('li:last').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
/* $(document).ready() indicates that the script will run
only when the page DOM is ready. '$()' is shorthand */
