from base_socket import Socket

class Server(Socket):
	def __init__(self, ip, port, users=None):
		super().__init__(ip, port)
		if users == None:
			self.users = {}
		else:
			self.users = users

	def broadcast_msg(self):
		pass
	
	def handle_clients(self):
		pass

	def start_server(self):
		pass

