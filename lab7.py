import socket

state = 0

def web_page():
    if state == 1:
        led="ON"
        led_state="led-on"
    else:
        led="OFF"
        led_state="led-off"
  
    html = """
    <html>
        <head> 
            <title>LED ON/OFF</title> 
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                html {
                    font-family: Helvetica; 
                    display:inline-block; 
                    margin: 0px auto; 
                    text-align: center;
                }
                h1 {
                    color: black; 
                    padding: 2vh;
                }
                p {
                    font-size: 1.5rem;
                }
                .button {
                    display: inline-block; 
                    background-color: white; 
                    border: 2px solid black; 
                    border-radius: 4px; 
                    color: black; 
                    padding: 16px 40px; 
                    text-decoration: none; 
                    font-size: 30px; 
                    margin: 2px; 
                    cursor: pointer;
                }
                .led-on {
                    display: inline-block;
                    width: 20px;
                    height: 20px;
                    background-color: red;
                    border: 2px solid black;
                }
                .led-off {
                    display: inline-block;
                    width: 20px;
                    height: 20px;
                    background-color: grey;
                    border: 2px solid black;
                }
            </style>
        </head>
        <body> 
            <h1>LED ON/OFF</h1> 
            <p>LED state: <strong>""" + led + """</strong></p>
            <div class=""" + led_state + """></div>
            <p><a href="/?led=on"><button class="button">ON</button></a></p>
            <p><a href="/?led=off"><button class="button">OFF</button></a></p>
        </body>
    </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8036))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6:
        print('LED ON')
        state = 1
    if led_off == 6:
        print('LED OFF')
        state = 0
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')
    conn.send(b'Content-Type: text/html\n')
    conn.send(b'Connection: close\n\n')
    conn.sendall(response.encode())
    conn.close()