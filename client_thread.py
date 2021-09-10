import socket, threading
from server_thread import ip, port

class Client():
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def connect(self, ip, port):
		self.s.connect((ip, port))
	
	def send_msg(self, msg):
		message = msg.encode('UTF-8')
		self.s.send(message)
	
	def close_con(self):
		self.s.close()
		
	
	
def main():
	test1 = Client()
	test1.connect(ip, port)
	while True:
		message = input('enter input: ')
		if message == 'close()':
			break
		test1.send_msg(message)
	test1.close_con()
	
	
	

if __name__ == '__main__':
	main()