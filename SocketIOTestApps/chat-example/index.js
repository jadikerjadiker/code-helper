var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var userAmt = 0


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
  
  socket.on('new user', function(username){
    userAmt++;
    io.emit('update userAmt', userAmt)
    io.emit('chat message', username+" just joined the chat!")
  });
  
  socket.on('disconnect', function(){
    userAmt--;
    io.emit('update userAmt', userAmt)
    io.emit('A user disconnected.');
  });
});

http.listen(8080, function(){
  console.log('listening on *:8080');
});