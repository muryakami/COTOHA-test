var url = location.href + 'read';
var reading = false;
var line_number = 0;
var instruction_text = "";
var brand_text = "";

function read() {
  $.ajax({
    url: url,
    type: 'POST',
    dataType: 'JSON',
    data: {
      'line_number': line_number
    }
  }).done(function (data) {
    if (reading) {
      $("#document").text(data.form);
      $("#result").text(data.score)
      line_number = data.next_line_number;
      if (line_number != 0) {
        setTimeout(read, data.text_length * 200);
      } else {
        setTimeout(stopReading, data.text_length * 200);
      }
    }
  });
}

function startReading() {
  $("button").text("ロウドク　ヤメ");
  reading = true;
}

function resumeReading() {
  $("button").text("ロウドク　ハジメ");
  reading = false;
}

function stopReading() {
  resumeReading();
  $("#document").text(instruction_text);
  $("#result").text("")
}

$(function () {
  $("button").click(function () {
    if (reading) {
      resumeReading();
    } else {
      let action = $(this).attr('id');
      if (action === 'read') {
        debugger;
        read();
      } else {
        read();
      }
      startReading();
    }
    return false;
  });
});

$(function () {
  instruction_text = $("#document").text();
});