const $ = window.$;

$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').is('.green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
