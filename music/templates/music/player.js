let canvasWidth = 500;
let audioEl = document.getElementById("audio");
let canvas = document.getElementById("progress").getContext("2d");
let ctrl = document.getElementById("audioControl");

/**
 * EventListener para cuando el audio esta cargado en el html
 */
audioEl.addEventListener("loadedmetadata", function() {
  let duration = audioEl.duration;
  let currentTime = audioEl.currentTime;
  document.getElementById("duration").innerHTML = convertElapsedTime(duration);
  document.getElementById("current-time").innerHTML = convertElapsedTime(
    currentTime
  );
  canvas.fillRect(0, 0, canvasWidth, 50);
});

/**
 * Funcion que da formato al tiempo de la cancion
 * @param {} inputSeconds
 */
function convertElapsedTime(inputSeconds) {
  let seconds = Math.floor(inputSeconds & 60);
  if (seconds < 10) {
    seconds = "0" + seconds;
  }
  let minutes = Math.floor(inputSeconds / 60);
  return `${minutes} : ${seconds}`;
}

/**
 * Permite al reproductor iniciar o pausar la musica
 */
function togglePlaying() {
  let play = ctrl.name == "Play";
  let method;
  if (play) {
    ctrl.name = "Pause";
    method = "play";
  } else {
    ctrl.name = "Play";
    method = "pause";
  }
  audioEl[method]();
}

/**
 * Metodo para actualizar la barra de progreso
 */
function updateBar() {
  //Limpiamos el canvas
  canvas.clearRect(0, 0, canvasWidth, 50);
  canvas.fillStyle = "#000";
  canvas.fillRect(0, 0, canvasWidth, 50);

  let currentTime = audioEl.currentTime;
  let duration = audioEl.duration;

  //Si la cancion termina se para la reproduccion
  if (currentTime === duration) {
    ctrl.innerHTML = "Play";
  }

  document.getElementById("current-time").innerHTML = convertElapsedTime(
    currentTime
  );

  //Pintamos el canvas segun el progreso de la canción
  let percentage = currentTime / duration;
  let progress = canvasWidth * percentage;
  canvas.fillStyle = "#FF0000";
  canvas.fillRect(0, 0, progress, 50);
}
