import socket


print("Welcome to Johans Rock-Paper-Sciccors game")

def serverSide():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('',60003))
    serverSocket.listen(5)
    clientSocket , _ = serverSocket.accept()
    return clientSocket

def clienSide(host):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((host,60003))
    return sock


ans = "?"
while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C)::")


if ans =="S":
    sock = serverSide()
    print("server up")

else:
    host = input("Enter the server's name or IP: ")
    sock = clienSide(host)



# The code lines that follow are the same for client and server
playerOneScore = 0
playerTwoScore = 0
playerMove = ''
otherPlayer = ''


while playerOneScore < 10 and playerTwoScore < 10 :

    playerMove = ''
    otherPlayer = ''

    while playerMove not in {"R", "P", "S"}:
        playerMove = input("({},{}) Make your Move :".format(playerOneScore, playerTwoScore))

    sock.sendall(bytearray(playerMove,'ASCII'))
    otherPlayer = sock.recv(1024).decode('ASCII')
    print("opponent's move: {}".format(otherPlayer))

    if playerMove + otherPlayer in 'RS PR SP' :
        playerOneScore +=1

    elif playerMove == otherPlayer:
        continue 

    else:
        playerTwoScore +=1

if playerOneScore > playerTwoScore:
    print("You won with {} against {}".format(playerOneScore,playerTwoScore))

else: 
    print("You lost with {} against {}".format(playerTwoScore,playerOneScore))

sock.close()
