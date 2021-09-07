import socket

#setttings
server = '127.0.0.1' 
port = 65432 

class Client:
	def __init__(self):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def connect(self, host, port):
		self.con.connect_ex((host, port))
	
	def send_msg(self, msg):
		self.con.send(bytes(msg, "UTF-8"))
	
	def rcv_msg(self):
		msg_rcv = self.con.recv(2048)
		print(msg_rcv.decode("UTF-8"))
		

def main():
	test1 = Client()
	test1.connect(server, port)

	while True:

		if test1.rcv_msg():
			test1.rcv_msg()
		
		message = input()

		if message != "close":
			test1.send_msg(message)
		else:
			break


if __name__ == '__main__':
	main()
