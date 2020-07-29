from socket import *
from threading import Thread

selfAddress = 'localhost'
selfPort = 7000
sendAddress = 'localhost'
sendPort = 12000
socket = socket(AF_INET, SOCK_DGRAM)
socket.bind((selfAddress, selfPort))


def get_message():
	message, address = socket.recvfrom(2048)
	print(address, ":", message)


thread = Thread(target = get_message, args = socket)
while True:
	thread.start()
	message = bytes(input(), 'utf-8')
	socket.sendto(message, (sendAddress, sendPort))