import socket
from server_thread import ip, port

class Client():
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def connect(self, ip, port):
		self.s.connect((ip, port))
	
	def close_con(self):
		self.s.close()
	
	def send_msg(self):
		while True:
			msg = input('')
			if msg == 'close()':
				break
			message = msg.encode('UTF-8')
			self.s.send(message)
		self.close_con()		
	
	
def main():
	test1 = Client()
	test1.connect(ip, port)
	test1.send_msg()
	test1.close_con()
	
	
	

if __name__ == '__main__':
	main()