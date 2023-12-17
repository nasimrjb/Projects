let city = "Tehran";
let apiKey = "ab343bcof0t2020acfeb0bf65d0c4516";

let apiUrl = `https://api.shecodes.io/weather/v1/current?query=${city}&key=${apiKey}`;

function displayWeather(response) {
  let temperature = Math.round(response.data.temperature.current);
  let temperatureElement = document.querySelector();
  temperatureElement.innerHTML = temperature;
}
axios.get(apiUrl).then(displayWeather);
