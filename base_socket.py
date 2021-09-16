import socket, threading

class Socket:
	def __init__(self, ip, port):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = ip
		self.port = port

	def connect(self):
		self.con.connect((self.ip, self.port))
	
	def shutdown(self, client_sock=None):
		if client_sock != None:
			client_sock.shutdown(socket.SHUT_RDWR)
			client_sock.close()
		self.con.shutdown(socket.SHUT_RDWR)
		self.con.close()
		
	def send_msg(self, msg, client_sock=None):
		try:
			if client_sock != None:
				client_sock.send(msg.encode("UTF-8"))
			else:
				self.con.send(msg.encode("UTF-8"))
		except KeyboardInterrupt:
				print('[GOODBYE]')
				self.s.close()
		
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


test = Socket('127.0.0.1', 6500)


