console.log("Loading chat.js");

const domainPreffix = "http://";
var socket = io.connect(domainPreffix + document.domain + ":" + location.port);

var form = $('form');
form.on('submit', function (post){
    post.preventDefault();
    let username = $('input.username').val();
    let message = $('input.message').val();

    socket.emit( 'send msg', {
        sender: username,
        content: message
    })

    $('input.message').val('').focus();
});

var updateChat = function( msg ) {
    if ( msg !== undefined && msg !== null
         && msg.sender !== undefined && msg.sender !== null
         && msg.content !== undefined && msg.content !== null )
    {
        let chatbox = $('div#chatcontentwrapper');
        chatbox.append("<div class='chatcontent'> <span class='chatcontent username'>" + msg.sender + " </span> </div> <div class='chatcontent'> <span class='chatcontent message'>" + msg.content + " </span </div>");
    }
}

socket.on( 'update', function( msg ) {
    console.log("Received chat update:: ");
    console.log(msg);
    updateChat( msg );
})

console.log("Loaded chat.js socket listening")
