import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(2)

listOfSockets = [sockL]

print("Listening on port {}".format(port))


while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:

        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        print("connection from {}".format(addr)) 
        msg ="{} (Connected)".format(sockClient.getpeername())

        for sockClient in listOfSockets[1:] :
            sockClient.sendall(bytearray(msg, "ASCII"))

    else:
        # Connected clients send data or are disconnecting
        
        data = sock.recv(2048)
       
        
        if not data :
            # A client disconnects
            msg ="{} (Disconnected)".format(sock.getpeername())
            sock.close()
            listOfSockets.remove(sock)
            
            for sockClient in listOfSockets[1:] :
                sockClient.sendall(bytearray(msg, "ASCII"))

        else:
            # data is a message from a client
            msg = "{} : {}".format(sock.getpeername(), data.decode("ASCII"))

            for sockClient in listOfSockets[1:] :
                sockClient.sendall(bytearray(msg, "ASCII"))

                
