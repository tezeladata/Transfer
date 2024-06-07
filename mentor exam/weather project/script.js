const button = document.getElementById("submit-button")
let apiUrl = "https://api.openweathermap.org/data/2.5/weather?q=Tbilisi&appid=8005e0a1974f974d81c999400dd12dc9";

// to show after call
let cityName = document.getElementById("city-name");
let timezone = document.getElementById("timezone");
let weather = document.getElementById("weather");
let image = document.getElementById("weather-img")

button.addEventListener("click", () => {
    const userCity = document.getElementById("input1").value;
    apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${userCity}&appid=8005e0a1974f974d81c999400dd12dc9`
    fetch(apiUrl).then(response => {
        return response.json();
    }).then(response => {
        // To show info
        cityName.innerHTML = response.name;
        timezone.innerHTML =  `Timezone: ${response.timezone}`
        weather.innerHTML = response.weather["0"].main + ", " +   response.weather["0"].description
    })
})
