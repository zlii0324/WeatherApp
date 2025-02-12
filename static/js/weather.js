async function getWeather() {
    const city = document.getElementById('city').value;
    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();
    
    if (data.error) {
        document.getElementById('weather-result').innerText = data.error;
    } else {
        const weatherInfo = `
            City: ${data.name}
            Temperature: ${data.main.temp} °C
            Feels Like: ${data.main.feels_like} °C
            Humidity: ${data.main.humidity} %
            Pressure: ${data.main.pressure} hPa
            Weather: ${data.weather[0].description}
            Wind Speed: ${data.wind.speed} m/s
        `;
        document.getElementById('weather-result').innerText = weatherInfo;
    }
}