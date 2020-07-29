from socket import *
selfAddress = '5.129.191.42'
selfPort = 11719
sendAddress = '192.168.100.5'
sendPort = 11719
socket = socket(AF_INET, SOCK_DGRAM)
socket.bind((selfAddress, selfPort))

while True:
	mode = input("Wanna check messages, send one or exit?(c/s/e): ")
	if mode.lower() == 'c':
		message, address = socket.recvfrom(2048)
		print(address, ":", message)
	elif mode.lower() == 's':
		message = bytes(input("Input your message: "), 'utf-8')
		socket.sendto(message, (sendAddress, sendPort))
	elif mode.lower() == 'e':
		break
socket.close()