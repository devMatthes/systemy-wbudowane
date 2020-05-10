import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3001))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been ok")
    clientsocket.send(bytes("Welcome to the server!\n", "utf-8"))
    result = 0
    clientsocket.send(bytes("Enter first value: ", "utf-8"))
    val1 = clientsocket.recv(1024)
    clientsocket.send(bytes("Enter second value: ", "utf-8"))
    val2 = clientsocket.recv(1024)
    clientsocket.send(bytes("Choose operation 1(add), 2(sub), 3(mul), 4(div): ", "utf-8"))
    operator = clientsocket.recv(1024)
    if int(operator) == 1:
        result = int(val1) + int(val2)
    elif int(operator) == 2:
        result = int(val1) - int(val2)
    elif int(operator) == 3:
        result = int(val1) * int(val2)
    elif int(operator) == 4:
        result = int(val1) / int(val2)
    result_as_string = str(result)
    clientsocket.send(bytes((result_as_string), "utf-8"))

s.close()
    
    
