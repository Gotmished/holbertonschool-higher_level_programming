$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (body) {
  $('#hello').text(body.hello);
});
