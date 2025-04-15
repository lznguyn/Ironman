$(document).ready(function () {
  // hien thi tin nhan
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
  }

  eel.expose(DisplayHood);
  function DisplayHood() {
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
  }
});
