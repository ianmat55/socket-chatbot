import threading, socket, sys

ip = '127.0.0.1' #localhost
port = 6500
# header = 10

class Server:
	def __init__(self, clients = [], nicks = []):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#Make addr resusable (able to start server again after shutdown)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.bind((ip, port))
		self.s.listen(5)

		#transfer storage to dictionary users which will hold client: nick
		self.clients = clients
		self.nicks = nicks
		self.count = 0

	def __repr__(self):
		structure = {
			"clientcount": self.count,
			"nickname list": self.nicks,
			"ip": ip,
			"port": port
		}
		return structure
	
	def broadcast(self, msg):
		for client in self.clients:
			client.send(msg.encode("UTF-8"))	

	def handle_client(self, client_sock, nick):
		while True:
			try:
				msg = client_sock.recv(2048).decode('UTF-8')
				if "__repr__" in msg:
					print(self.__repr__())
					continue
				self.broadcast(msg)
				print(msg)
				if not msg:
					break
			except:
				print(f"{nick} has left the chat")
				self.clients.remove(client_sock)
				self.count -= 1
				self.nicks.remove(nick)
				print(f"users: {self.nicks}")
				print(self.count)
				client_sock.close()
				break	

	def start(self):
		print("Initializing server...")
		print("HELLO WORLD")

		while True:
			
			try:
				if self.count != 0:
					print(f"{self.count} client(s) in server")
					print(f"users: {self.nicks}")

				client_sock, addr = self.s.accept()
				print(f"[Connected] {addr}")
				client_sock.send("NICK".encode("UTF-8"))
				nick = client_sock.recv(2048).decode("UTF-8")

				self.nicks.append(nick)
				self.clients.append(client_sock)
				self.count += 1

				message = f"{nick} has joined the chat"
				client_sock.send("Welcome to the server\n".encode("UTF-8"))
				self.broadcast(message)

				conn = threading.Thread(target=self.handle_client, args=(client_sock, nick))
				conn.start()

			#Shutdown server of ctrl-c	
			except KeyboardInterrupt:
				print('[GOODBYE]')
				self.s.close()
				break

def main():
	server = Server()
	server.start()

if __name__ == '__main__':
	main()
