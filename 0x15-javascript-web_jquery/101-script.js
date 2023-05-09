// adds, removes and clears LI elements from a list when the user clicks

$('document').ready(() => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li:last()').remove();
  });

  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
