import socket, threading, time
from server_thread import ip, port

class Client():
	def __init__(self, nick=input('What is your username: ')):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.nick = nick 

	def connect(self, ip, port):
		self.s.connect((ip, port))
	
	def close_con(self):
		self.s.close()
	
	def send_msg(self):
		while True:
			msg = input('')
			if msg == 'close()':
				break
			self.s.send(f"[{self.nick}] {msg}".encode("UTF-8"))
		self.close_con()	

	def recv_msg(self):
		while True:
			msg = self.s.recv(2048).decode("UTF-8")
			if msg == "NICK":
				self.s.send(self.nick.encode("UTF-8"))
			else:
				print(msg)
	
			
def main():
	test1 = Client()
	test1.connect(ip, port)
	recv_thread = threading.Thread(target=test1.recv_msg)
	recv_thread.start()
	send_thread = threading.Thread(target=test1.send_msg)
	send_thread.start()
	
	

if __name__ == '__main__':
	main()