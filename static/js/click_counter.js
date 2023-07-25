

document.addEventListener('DOMContentLoaded', function() {
  var buttons = document.getElementsByClassName('btn-counter');

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      var countSpan = this.nextElementSibling;
      var count = parseInt(countSpan.textContent);
      count++;
      countSpan.textContent = count;
    });
  }

  var acceptBtn = document.getElementById('acceptBtn');
  acceptBtn.addEventListener('click', function() {
    var counts = [];
    var countSpans = document.getElementsByClassName('count');

    for (var i = 0; i < countSpans.length; i++) {
      var count = parseInt(countSpans[i].textContent);
      counts.push(count);
    }

    console.log(counts); // Do something with the counts
  });
});
