from socket import *

serverName = '5.129.191.42'
serverPort = 778
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
	message = input('Input lowercase message(print @exit to exit): ')
	if message == '@exit': break
	message = bytes(message, 'utf-8')
	clientSocket.sendto(message, (serverName, serverPort))
clientSocket.close()