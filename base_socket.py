import socket

class Socket:
	def __init__(self):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#not adding ip and port to init because we are connecting to ourself
	def connect(self, ip, port):
		self.con.connect((ip, port))
	
	def shutdown(self):
		self.con.shutdown(socket.SHUT_RDWR)
		self.con.close()
		
	def send_msg(self, msg):
		self.con.send(msg.encode("UTF-8"))
		
	def rcv_msg(self):
		msg_rcv = self.con.recv(2048)
		print(msg_rcv.decode("UTF-8"))
	
	
	#server functions
	def listen(self, ip, port):
		self.con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.con.bind((ip, port))
		self.con.listen(5)
	
	def accept(self):
		client_sock, addr = self.con.accept()
		return client_sock, addr
	
	#print info
	def __repr__(self):
		structure = f"family: {self.con.family}, type: {self.con.type}, ip: {self.ip}, port: {self.port}"
		return structure



