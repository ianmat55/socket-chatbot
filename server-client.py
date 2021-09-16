from base_socket import Socket
import threading

class Server(Socket):
	def __init__(self, ip, port, users=None):
		super().__init__(ip, port)
		if users == None:
			self.users = {}
		else:
			self.users = users
	
	def start(self):
		print("Initializing server...")
		while True:
			try:
				client_sock = self.s.accept()
				client_sock.send("NICK".encode("UTF-8"))
				nick = client_sock.recv(2048).decode("UTF-8")
				self.users[client_sock] = nick

			#Shutdown server of ctrl-c	
			except KeyboardInterrupt:
				print('[GOODBYE]')
				self.s.close()
				break
	
	def transcribe(self):
		pass

class Client(Socket):
	def __init__(self, ip, port, site, nick=input('What is your username: ')):
		super().init(ip, port)
		self.nick = nick
		self.site = site
	
	def scraper(self, site):
		pass
	
	def start(self):
		pass


