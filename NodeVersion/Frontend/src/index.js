import './index.css'

var serverIp = "192.168.0.4:5505";
/*imports the socket.io client*/
const io = require("socket.io-client"),
/*Creates a client that connects ot server at the specified address*/
client = io.connect(serverIp);

var tempLabel = document.getElementById("tempLabel");
var humidityLabel = document.getElementById("humidityLabel");
var hourlyHigh = document.getElementById("hourlyHigh");
var hourlyLow = document.getElementById("hourlyLow");
var dailyHigh = document.getElementById("dailyHigh");
var dailyLow = document.getElementById("dailyLow");
var weeklyHigh = document.getElementById("weeklyHigh");
var weeklyLow = document.getElementById("weeklyLow");

client.on("temp",function(temp){
    tempLabel.innerText = temp;
})

client.on("humidity",function(humidity){
    humidityLabel.innerText = humidity;
})

client.on("hourly",function(low, high){
    hourlyLow.innerText = low;
    hourlyHigh.innerText = high;
})

client.on("daily",function(low, high){
     dailyLow.innerText = low;
     dailyHigh.innerText = high;
})

client.on("weekly",function(low, high){
    weeklyLow.innerText = low;
    weeklyHigh.innerText = high; 
})