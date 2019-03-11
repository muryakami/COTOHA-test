var url = location.href;
var reading = false;
var line_number = 0;
var instruction_text = "";
var brand_text = "";

function read() {
  $.ajax({
    url: url + 'read',
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

function parse() {
  $.ajax({
    url: url + 'parse',
    type: 'POST',
    dataType: 'JSON',
    data: {
      'line_number': line_number
    }
  }).done(function (data) {
    if (reading) {
      debugger;
      $("#document").text(data.sentence);
      $("#result").text(data.kana)
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
  $("button").text("Stop");
  reading = true;
}

function resumeReading() {
  $("button").text("Start");
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
        read();
      } else if (action == 'parse') {
        parse();
      } else {
        debugger;
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