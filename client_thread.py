import socket, threading
from server_thread import ip, port

class Client():
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def connect(self, ip, port):
		self.s.connect((ip, port))
	
	def send_test(self, msg):
		message = msg.encode("UTF-8")
		self.s.send(message)
	
	
def main():
	test1 = Client()
	test1.connect(ip, port)
	
	
	

if __name__ == '__main__':
	main()