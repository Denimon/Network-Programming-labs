
import socket

#date
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

serverSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 8080))
serverSocket.listen(10)

print("Johans HTTP Server")

while True:
    print('\nListening...\n')
    (clientSocket, addr) = serverSocket.accept()
    print('connection from {}'.format(addr))

    while True:
        data = clientSocket.recv(1024)
        decodedData = data.decode('ascii')

        if not data : 
            break

        htmlBody = "<html><body><h1>Your browser sent the following request</h1><pre>{}</pre></body></html>".format(decodedData)
        print('recieved: ', decodedData)

        now = datetime.now()
        stamp = mktime(now.timetuple())

        resHeaders = {
        'Date' : format_date_time(stamp),     
        'Content-Type': 'text/html; charset=iso-8859-1',
        'Content-Length': len(htmlBody),
        'Connection': 'close',
        }

        resHeaders_raw = ''.join('%s: %s\r\n' % (key , value) for key, value in resHeaders.items())

        clientSocket.send(bytearray("HTTP/1.1 200 OK\n", 'ascii'))
        clientSocket.send(bytearray(resHeaders_raw,'ascii'))
        clientSocket.send(bytearray("\n", "ASCII"))
        clientSocket.send(bytearray(htmlBody, 'ascii'))
    
    clientSocket.close()    