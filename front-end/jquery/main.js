$(document).ready(function () {
  $('#change-color').click(function () {
    $('h1').toggleClass('red-title');
  });
  $('#hide-text').click(function () {
    $('p').toggle();
  });
  $('#activate-dark-mode').click(function () {
    $('body').toggleClass('dark-mode');
  });
});

// vanilla js for comparison
function displayDate(id) {
  document.getElementById('date').innerHTML = Date();
}
