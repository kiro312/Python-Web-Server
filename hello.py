from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 9900))

serverSocket.listen(1)

while True:
    print("Server is running")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)

        filename = message.split()[1].decode('utf-8').strip("/")
        print(filename)
        f = open(filename)
        outputdata = f.read()
        f.close()

        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        connectionSocket.send('404 Not Found'.encode())
        connectionSocket.close()

serverSocket.close()
 