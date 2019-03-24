// let url = location.href;
let url = location.origin;
let reading = false;
let line_number = 0;
let instruction_text = "";
let brand_text = "";

function read() {
  $.ajax({
    url: url + "/read",
    type: "POST",
    dataType: "JSON",
    data: {
      line_number: line_number
    }
  }).done(function(data) {
    if (reading) {
      $("#document").text(data.form);
      $("#result").text(data.score);
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
    url: url + "/parse",
    type: "POST",
    dataType: "JSON",
    data: {
      line_number: line_number
    }
  }).done(function(data) {
    if (reading) {
      $("#document").text(data.sentence);
      $("#result").text(data.kana);
      line_number = data.next_line_number;
      if (line_number != 0) {
        setTimeout(parse, data.text_length * 200);
      } else {
        setTimeout(stopReading, data.text_length * 200);
      }
    }
  });
}

function keyword() {
  $.ajax({
    url: url + "/keyword",
    type: "POST",
    dataType: "JSON",
    data: {
      line_number: line_number
    }
  }).done(function(data) {
    if (reading) {
      $("#document").text(data.sentence);
      $("#result").text(data.form);
      line_number = data.next_line_number;
      if (line_number != 0) {
        setTimeout(keyword, data.text_length * 200);
      } else {
        setTimeout(stopReading, data.text_length * 200);
      }
    }
  });
}

function user_attribute() {
  $.ajax({
    url: url + "/user_attribute",
    type: "POST",
    dataType: "JSON",
    data: {
      line_number: line_number
    }
  }).done(function(data) {
    if (reading) {
      $("#document").text(data.sentence);
      addList("#result", data.result);
      line_number = data.next_line_number;
      if (line_number != 0) {
        Promise.resolve()
          .then(() => wait(data.text_length * 200))
          .then(() => user_attribute())
          .then(() => removeList("#result"))
          .catch(() => console.error("Something wrong!"));

        // let promise = new Promise(function(resolve, reject) {
        //   setTimeout(function() {
        //     resolve(user_attribute());
        //   }, data.text_length * 200);
        // });
        // promise
        //   .then(function() {
        //     removeList("#result");
        //   })
        //   .catch(function() {
        //     console.error("Something wrong!");
        //   });
      } else {
        setTimeout(stopReading, data.text_length * 200);
      }
    }
  });
}

// milliseconds後にresolveするpromiseオブジェクトを戻す関数
const wait = milliseconds =>
  new Promise(resolve => setTimeout(resolve, milliseconds));

function startReading() {
  $("#action").text("Stop");
  reading = true;
}

function resumeReading(menu) {
  $("#action").text("Start");
  reading = false;
}

function stopReading() {
  resumeReading();
  $("#document").text(instruction_text);
  $("#result").text("");
}

function addList(element, result) {
  // li に追加する内容
  let ul = $("<ul>")
    .addClass("list")
    .css("list-style", "none"); // ul タグを生成して ul に追加
  Object.keys(result).forEach(function(key) {
    let val = this[key]; // this は obj
    let li = $("<li>").text(key + ": " + val); // li タグを生成してテキスト追加
    ul.append(li); // ul に生成した li タグを追加
  }, result);
  $(element)
    .append(ul)
    .removeClass("col mx-2"); // insertを#result内に追加
}

function removeList(element) {
  $(element + ":first").empty();
}

function plotres(response, prefix) {
  for (var key in response) {
    if (typeof response[key] == "object") {
      if (Array.isArray(response[key])) {
        // 配列の場合は forEach で要素ごとにに再帰呼び出し
        response[key].forEach(function(item) {
          plotres(item, prefix + " " + key);
        });
      } else {
        // 連想配列はそのまま再帰呼び出し
        plotres(response[key], prefix + " " + key);
      }
    } else {
      // 配列や連想配列でなければキーの値を表示
      console.log(prefix + " " + key + ": " + response[key]);
    }
  }
}

$(function() {
  $("#action").click(function() {
    if (reading) {
      resumeReading();
    } else {
      let action = $(this).attr("name");
      switch (action) {
        case "read":
          read();
          break;
        case "parse":
          parse();
          break;
        case "keyword":
          keyword();
          break;
        case "user_attribute":
          user_attribute();
          break;
        default:
          debugger;
          return false;
      }
      startReading();
    }
    return false;
  });
});

$(function() {
  instruction_text = $("#document").text();
});

$(function() {
  $(".dropdown-item").click(function() {
    if (reading) {
      stopReading();
    }
    $("#action")
      .text($(this).text())
      .attr("name", $(this).attr("id"));
  });
});
