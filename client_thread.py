import socket, threading
from server_thread import ip, port

class Client():
	def __init__(self, nickname = input("Enter username: ")):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.nickname = nickname
		print(self.nickname)
	
	def connect(self, ip, port):
		self.s.connect((ip, port))
	
	
	def rcv_msg(self):
		while True:
			try:
				message = self.s.recv(2048).decode("UTF-8")
				if message == 'NICK':
					self.s.send(self.nickname.encode("UTF-8"))
				else:
					print(message)
			except:
				print("An error has occurred")
				self.s.close()
				break
			
	def send_msg(self):
		while True:
			message = f"{self.nickname}: {input('')}"
			if message == f"{self.nickname}: close":
				break
			else:
				self.s.send(message.encode("UTF-8"))
	
	def thread(self):
		recv_thread = threading.Thread(target=self.rcv_msg)
		recv_thread.start()

		send_thread = threading.Thread(target=self.send_msg)
		send_thread.start()


	

def main():

	client1 = Client()
	client1.connect(ip, port)
	client1.thread()

	

if __name__ == '__main__':
	main()