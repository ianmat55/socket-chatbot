from base_socket import Socket

class Server(Socket):
	def __init__(self, ip, port, users=None):
		super().__init__(ip, port)
		if users == None:
			self.users = {}
		else:
			self.users = users
	
	def transcribe(self):
		pass

	def handle_client(self, client_sock, nick):
		while True:
			try:
				msg = client_sock.recv(2048).decode('UTF-8')
				for client in self.user.keys():
					self.send(msg, client)

				print(msg)
				if not msg:
					break
			except:
				print(f"{nick} has left the chat")
				del self.clients[nick]
				print(f"users: {self.users.values()}")
				client_sock.close()
				break	

	def start(self):
		print("Initializing server...")
		while True:
			try:
				client_sock = self.s.accept()
				client_sock.send("NICK".encode("UTF-8"))
				nick = client_sock.recv(2048).decode("UTF-8")
				self.users[client_sock] = nick

				#start thread
				self.thread(self.handle_client, (client_sock, nick))

			#Shutdown server of ctrl-c	
			except KeyboardInterrupt:
			       print('[GOODBYE]')
			       self.s.close()
			       break


class Client(Socket):
	def __init__(self, ip, port, nick, site=None):
		super().__init__(ip, port)
		self.nick = nick
		self.site = site
	
	def read_file(self, file):
		with open(str(file)) as f:
			lines = f.readlines()
			for line in lines:
				self.send_msg(line)			
	def recv_msg(self):
		while True:
			try:
				msg = self.con.recv(2048).decode("UTF-8")
				if msg == "NICK":
					self.con.send(self.nick.encode("UTF-8"))
				else:
					print(msg)

			except:
				print('[GOODBYE]')
				self.con.close()
				break	
	

#user = input('what is your name? ')
# test = Client('127.0.0.1', 6500, user)
# test.connect()

# test.thread(test.recv_msg)

# test.read_file('texts/poem.txt')

# test.shutdown()