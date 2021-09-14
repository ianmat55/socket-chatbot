import socket

class Client:
	def __init__(self, ip, port):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ip = ip
		self.port = port
		
	def connect(self):
		self.con.connect((self.ip, self.port))
		
	def send_msg(self, msg):
		self.con.send(bytes(msg, "UTF-8"))
		
	def rcv_msg(self):
		msg_rcv = self.con.recv(2048)
		print(msg_rcv.decode("UTF-8"))

	def __repr__(self):
		structure = f"con: {self.con}, ip: {self.ip}, port: {self.port}"
		
		return structure

if __name__ == '__main__':
	pass
