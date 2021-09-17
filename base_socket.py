import socket, threading

class Socket:
	def __init__(self, ip, port):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = ip
		self.port = port

	def connect(self, user=None):
		self.con.connect((self.ip, self.port))
		print(f"* Welcome {user}")

	
	def shutdown(self, client_sock=None):
		if client_sock != None:
			client_sock.shutdown(socket.SHUT_RDWR)
			client_sock.close()
		self.con.shutdown(socket.SHUT_RDWR)
		self.con.close()

	# open a txt file, send the contents
	# def read_file(self, file):
	# 	with open(str(file)) as f:
	# 		lines = f.readlines()
	# 		for line in lines:
	# 			self.con.send(line.encode("UTF-8"))
		
	def send_msg(self):
		while True:
			try:
				msg = input('>> ')
				if msg == 'close()':
					self.con.close()
				else:
					self.con.send(f"{msg}".encode("UTF-8"))

			except KeyboardInterrupt:
				print('[GOODBYE]')
				self.con.close()
				break 
		
		
	def recv_msg(self, client_sock=None):
		if client_sock != None:
			msg_recv = client_sock.recv(2048)
		else: 
			msg_recv = self.con.recv(2048)

		return msg_recv.decode("UTF-8")
	
	def thread(self, func, params=None):
		if params == None:
			conn = threading.Thread(target=func)
			conn.start()
		else:
			conn = threading.Thread(target=func, args=(params))
			conn.start()

	#server functions
	def listen(self):
		self.con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.con.bind((self.ip, self.port))
		self.con.listen(5)
	
	def accept(self):
		self.con.accept()
	
	#print info

	def get_constants(self, pref):
		return dict((getattr(self.con,n), n) for n in dir(self.con) if n.startswith(pref))

	def __repr__(self):
		families = str(self.get_constants('AF_'))
		types = str(self.get_constants('SOCK_'))
		protocols = str(self.get_constants("IPPROTO_"))

		structure = f"family: {families}, type: {types}, ip: {self.ip}, port: {self.port}, protocol: {protocols}"
		return structure


#Server class
class Server(Socket):
	def __init__(self, ip, port, users=None):
		super().__init__(ip, port)
		if users == None:
			self.users = {}
		else:
			self.users = users
	

	def broadcast(self, msg):
		for client in self.users.keys():
			client.send(msg.encode("UTF-8"))	

	
	# def transcribe(self, msg):
	# 	with open('transcription.txt', 'w') as trans:
	# 		trans.write(msg)

	def handle_client(self, client_sock, nick):
		while True:
			msg = client_sock.recv(2048).decode('UTF-8')
			self.broadcast(msg)
			print(msg)
			if not msg:
				print(f"{nick} has left the chat")
				for key, value in self.users.items():
					if value == nick:
						del self.users[key]
						break
				print(f"users: {[user for user in self.users.values()]}")
				client_sock.close()
				break	

	def start(self):
		print("Initializing server...")
		while True:
			try:
				client_sock, addr = self.con.accept()
				client_sock.send("NICK".encode("UTF-8"))
				nick = client_sock.recv(2048).decode("UTF-8")
				self.users[client_sock] = nick

				# Turn this into a cmd line server function 
				print(f"users: {[user for user in self.users.values()]}")

				#start thread
				self.thread(self.handle_client, (client_sock, nick))

			#Shutdown server of ctrl-c	
			except KeyboardInterrupt:
			       print('[GOODBYE]')
			       self.con.close()
			       break



#Client class
class Client(Socket):
	def __init__(self, ip, port, nick):
		super().__init__(ip, port)
		self.nick = nick
		

	def recv_msg(self):

		self.thread(self.send_msg)

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
	




