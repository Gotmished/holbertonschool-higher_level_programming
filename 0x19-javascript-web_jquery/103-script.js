$(document).ready(function () {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    $.get('https://stefanbohacek.com/hellosalut/?lang=' + language, function (body) {
      $('#hello').text(body.hello);
    });
  });
  $(document).on('keypress', function (event) {
    if (event.which === 13) {
      const language = $('#language_code').val();
      $.get('https://stefanbohacek.com/hellosalut/?lang=' + language, function (body) {
        $('#hello').text(body.hello);
      });
    }
  });
});
