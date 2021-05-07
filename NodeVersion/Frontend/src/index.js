import './index.css'

var serverIp = "192.168.0.15:5505";
/*imports the socket.io client*/
const io = require("socket.io-client"),
/*Creates a client that connects ot server at the specified address*/
client = io.connect(serverIp);

client.on("test",function(data){
    console.log(data);
})