
   const roomName = JSON.parse(document.getElementById('room-name').textContent);
        var username = JSON.parse(document.getElementById('curUser').textContent);;
        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + roomName
            + '/'
        );
        //Pronalzasenje ulogovanog korisnika


        //Ucitavanje poruka 
        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            var newDiv = document.createElement("p");
            newDiv.classList.add("mystyle");
            newDiv.classList.add("col-md-6");
            if (data.user === username){
              newDiv.classList.add("offset-md-6");
            }
            newDiv.innerHTML = data.user + ': ' + data.message;
            document.querySelector('#chat-log').appendChild(newDiv);
           
            
            var kocka = document.getElementById("chat-log");
            kocka.scrollTop = kocka.scrollHeight;
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
        //Enter Radi kao Send
        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message,
                'user': username
            }));
            messageInputDom.value = '';
        };