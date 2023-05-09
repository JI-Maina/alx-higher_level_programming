// fetches from api  and displays the value of hello from that fetch in the
// HTML tag DIV#hello

$('document').ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
  });
});
