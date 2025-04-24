$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });
  // Siri configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 840,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    autostart: true,
  });
  // siri message animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
      sync: true,
    },
    out: {
      effect: "bounceOut",
      sync: true,
    },
  });

  //Microphone animation
  $("#MicBtn").click(function (e) {
    eel.playAssistantSound();
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.allcommand()();
  });
  // Tắt Siri/micro khi nhấn vào bất kỳ nơi nào trên màn hình
  $(document).click(function (e) {
    // Kiểm tra nếu click không phải là trên nút microphone
    if (!$(e.target).closest("#MicBtn").length) {
      $("#SiriWave").attr("hidden", true);
      $("#Oval").attr("hidden", false);
    }
  });

  function doc_keyUp(e) {
    if (e.key === "j" && e.metaKey) {
      eel.playAssistantSound();
      $("Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allcommand()();
    }
  }
  document.addEventListener("keyup", doc_keyUp, false);
});
