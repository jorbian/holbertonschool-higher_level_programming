const $ = window.$;

$(document).ready(
  () =>
    () => $('#red_header').click(
      () => $('header').css({ color: 'red' })
    )
);
