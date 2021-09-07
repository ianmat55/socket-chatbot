import socket

#socket chat between client(s) and server

server = '127.0.0.1' # Standard loopback interface addy (localhost)
port = 65432 # Non-privileged ports are > 1023
users = []

def server_init():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket(address family for IPv4, socket type for TCP)
	s.bind((server, port)) #bind, associates socket with specific network and port number
	s.listen(5) #queus up to 5 connect requests

	while True:
		clientcon, addr = s.accept() 
		users.append(clientcon)

		with clientcon:
			print(f"Connection from {addr}")
			clientcon.send(bytes(f"Welcome to the server", "UTF-8"))
			while True:
				data = clientcon.recv(2048)
				print(data)

				if not data:
					break
				clientcon.sendall(data)

if __name__ == '__main__':
	server_init()
