const $ = window.$;
const frapi = 'https://stefanbohacek.com/hellosalut/?lang=fr';

$(document).ready(function () {
  $.get(frapi, function (data) {
    $('DIV#hello').append(data.hello);
  });
});
