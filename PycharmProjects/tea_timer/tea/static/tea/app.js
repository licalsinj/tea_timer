var timeRemaining = new Number();
var setTime = new Number();
var isRunning = false;

var PauseButton = "<button type=\"button\" class=\"btn btn-success btn-xs\" onClick=\"PauseButtonLogic()\">\n" +
    "                   <span class=\"glyphicon glyphicon-pause\"></span> Pause\n" +
    "              </button>"
var ResumeButton = "<button type=\"button\" class=\"btn btn-success btn-xs\" onClick=\"PauseButtonLogic()\">\n" +
    "                   <span class=\"glyphicon glyphicon-play-circle\"></span> Resume\n" +
    "              </button>"
var PauseButton2 = "<input type=\"button\" value=\"Pause\" onClick=\"PauseButtonLogic()\"/>";
var ResumeButton2 = "<input type=\"button\" value=\"Resume\" onClick=\"PauseButtonLogic()\"/>";
var button_id = "";

function setupTimer(steep_time, butt_id){
    document.getElementById("start_button").hidden = false;
    isRunning = false;
    if(butt_id.id){
        button_id = butt_id.id;
    }
    document.getElementById("pause").innerHTML = "";

    if(steep_time){
        setTime = steep_time;
        timeRemaining = setTime;
        var outputString = "setTime is: " + setTime + "<br />";
        outputString += "remaining time is: " + timeRemaining + "<br />";
        document.getElementById("output").innerHTML = outputString;
    }
}
function startTimer(){
  timeRemaining = setTime;
  document.getElementById("pause").innerHTML = PauseButton;
  document.getElementById("start_button").hidden = true;
  isRunning = true;
}
function runTimer(){
    if(isRunning){
      timeRemaining -= 1;

      var outputString = "setTime is: " + setTime + "<br />";
      outputString += "remaining time is: " + timeRemaining + "<br />";

      if(timeRemaining <= 0){
          outputString = "<H1>TIMES UP!</H1>";
          isRunning = false;
          document.getElementById(button_id).value = "Finished";
          document.getElementById(button_id).disabled = true;
          document.getElementById(button_id).class = "btn btn-success btn-xs";

          document.getElementById("pause").innerHTML = "";
      }
      document.getElementById("output").innerHTML = outputString;
    }
}
function PauseButtonLogic(){
  isRunning = !isRunning;
  if(!isRunning){
    document.getElementById("pause").innerHTML = ResumeButton;
  }
  else{
    document.getElementById("pause").innerHTML = PauseButton;
  }
}
