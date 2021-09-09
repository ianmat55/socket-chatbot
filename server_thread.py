import threading, socket

ip = '127.0.0.1' #localhost
port = 6500

class Server:
	def __init__(self, clients = [], nicks = []):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clients = clients
		self.nicks = nicks
	
	def broadcast_msg(self, msg):
		for client in self.clients:
			client.send(msg)
	
	def handle_clients(self, client):
		while True:
			try:
				message = client.recv(2048)
				self.broadcast_msg(message)	
			except:
				index = self.clients.index(client)
				self.clients.remove(client)
				client.close()
				nickname = self.nicks[index]
				self.broadcast(f"{nickname} as left chat".encode("UTF-8"))
				self.nicks.remove(nickname)
				break
	
	def rcv_msg(self):
		while True:
			clientcon, addr = self.s.accept()
			print(f"{str(addr)} connected")

			clientcon.send("NICK".encode("UTF-8"))
			nickname = clientcon.recv(2048).decode("UTF-8")
			self.nicks.append(nickname)
			self.clients.append(clientcon)

			print(f"{self.nicks}")
			self.broadcast_msg(f"{nickname} has joined the chat!\n".encode("UTF-8"))
			clientcon.send("Connected to server...".encode("UTF_8"))

			thread = threading.Thread(target=self.handle_clients, args=(clientcon,))
			thread.start()

	def start(self, ip, port):
		self.s.bind((ip, port))
		self.s.listen(5)
	

def main():
	server1 = Server()
	server1.start(ip, port)
	print("SERVER INITIALIZED")
	server1.rcv_msg()

if __name__ == '__main__':
	main()
