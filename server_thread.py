import threading, socket

ip = '127.0.0.1' #localhost
port = 6500
# header = 10

class Server:
	def __init__(self, clients = [], nicks = []):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((ip, port))
		self.s.listen(5)

		self.clients = clients
		self.nicks = nicks

	def broadcast(self, msg):
		for client in self.clients:
			client.send(msg.encode("UTF-8"))	

	def handle_client(self, client_sock, addr):
		self.clients.append(client_sock)
		print(f"[Connected] {addr}")
		while True:
			msg = client_sock.recv(2048).decode('UTF-8')
			self.broadcast(msg)
			print(msg)
			if not msg:
				break
		client_sock.close()	

	def start(self):
		print("Initializing server...")
		print("HELLO WORLD")

		while True:
			client_sock, addr = self.s.accept()
			conn = threading.Thread(target=self.handle_client, args=(client_sock, addr))
			conn.start()
			

def main():
	server = Server()
	server.start()

if __name__ == '__main__':
	main()
