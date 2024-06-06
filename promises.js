// let weather;
// getWeather()

// function getWeather(){
//     setTimeout(() => {
//         weather = "Sunny";
//     })
// }

// getWeather(displayIcon)
// function displayIcon(data){
//     if(data === "Sunny") return "a"
//     if (data === "Cloudy") return "b"
// }

// function getWeather(callback){
//     setTimeout(() => {
//         callback("Sunny")
//     }, 2000)
// }


// When speaking about promises, there are always two people:
// Person who makes promises and person who the promise was made to


// Maker is function that makes promise function and returns it
// Receiver is part of the code that calls maker and receives promise



// // Promise maker:
// function getWeather(){
//     return new Promise(function(resolve, reject){
//         setTimeout(function() {
//             reject("Error")
//         })
//     })
//     // it returns promise object
// }

// // Promise receiver:
// getWeather()


// function getWeather() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve("Sunny")
//         }, 100)
//     })
// }

// function getWeatherIcon(weather){
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             switch(weather){
//                 case "Sunny":
//                     resolve ("☀️")
//                     break
//                 case "Cloudy":
//                     resolve("☁️")
//                     break
//                 case "Cloudy":
//                     resolve("🌧️")
//                     break
//                 default:
//                     reject("No icon found")
//             }
//             resolve("Sunny")
//         }, 100)
//     })
// }

// function onSuccess(data){
//     console.log(`Success: ${data}`)
// }

// function onError(error){
//     console.log(`Error: ${error}`)
// }

// getWeather()
//     .then(getWeatherIcon) // whatever gets resolved, goes here
//     .then(onSuccess)
//     .catch(onError) // only called when reject is written



function func1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            reject("404")
        }, 100)
    })
}

function func2() {
    console.log(func2)
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("🏀")
        }, 100)
    })
}

function onSuccess(data){
    console.log(`Success: ${data}`)
}
function onError(errorCode){
    console.log(`Error: ${errorCode}`)
}


func1()
    .then(func2)
    .then(onSuccess)
    .catch(onError)