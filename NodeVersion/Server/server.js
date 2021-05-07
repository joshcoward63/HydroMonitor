;/*This file creates a Nodejs server that listens for command from Misty Client and frontend Web Client*/
// const { Console, countReset } = require('console');
var express = require('express');
var app = express();
var serverPort = 5005;
/*Server is listening on port 5000*/
var server = app.listen(serverPort);

app.use(express.static('public'));
console.log("Listening on port " + serverPort);

var socket = require('socket.io');

/*Starts socketio server*/ 
var io = socket(server);


io.sockets.on('connection', newConnection);
 function newConnection(socket){
	console.log("bopbs");
 	console.log("new connection: " + socket.id);
	  io.to(socket.id).emit("test", "boobs");
	  socket.broadcast.emit("test","boobs");

	socket.on("temp",function(temp){
		socket.broadcast.emit("temp", temp);
	})

	socket.on("humidity",function(humidity){
		socket.broadcast.emit("humidity", humidity);
	})

	socket.on("hourly",function(low, high){
		socket.broadcast.emit("hourly", low, high);
	})

	socket.on("daily",function(low, high){
		socket.broadcast.emit("daily", low, high);
	})

	socket.on("weekly",function(low, high){
		socket.broadcast.emit("weekly", low, high);
	})
}