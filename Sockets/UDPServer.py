from socket import *

serverName = '5.129.191.42'
serverPort = 778
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print("The server is ready to recieve")

while True:
	message = input()
	
	print("ClientAddress: ", clientAddress, "\n")
	serverSocket.sendto(modifiedMessage, clientAddress)