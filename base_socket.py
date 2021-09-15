import socket

class Socket:
	def __init__(self, ip, port):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = ip
		self.port = port

	def connect(self):
		self.con.connect((self.ip, self.port))
	
	def shutdown(self):
		self.con.shutdown(socket.SHUT_RDWR)
		self.con.close()
		
	def send_msg(self, msg):
		self.con.send(msg.encode("UTF-8"))
		
	def recv_msg(self, sock):
		msg_recv = sock.recv(2048)
		print(msg_recv.decode("UTF-8"))

		return msg_recv
	
	#server functions
	def listen(self):
		self.con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.con.bind((self.ip, self.port))
		self.con.listen(5)
	
	def accept(self):
		self.con.accept()
	
	#print info
	def __repr__(self):
		structure = f"family: {self.con.family}, type: {self.con.type}, ip: {self.ip}, port: {self.port}"
		return structure



