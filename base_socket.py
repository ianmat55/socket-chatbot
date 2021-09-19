# Built with python version 3.8.10
# email: ianmat55@gmail.com

import socket, threading
import ux, os
from rich.console import Console
from rich.table import Table

class Client:
	def __init__(self, ip, port, nick=None):
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.ip = ip
		self.port = port
		
		# username of client, need input when integrating class, can't put in init or 
		# itll run on import
		self.nick = nick 


		# Ric text color text customization
		custom_theme = ux.theme
		self.console = Console(theme=custom_theme)
		self.console.print(f"{ux.title}", style="title") # imported ascii art title
		
	# turned threading into a function because TDD principles?
	def thread(self, func, params=None):
		
		if params == None:
			conn = threading.Thread(target=func)
			conn.start()
		else:
			conn = threading.Thread(target=func, args=(params))
			conn.start()
	
	def connect(self):
		try:	
			# prints help table at startup. Imported from ux module 
			ux.print_client_help()

			self.con.connect((self.ip, self.port))
			self.thread(self.recv_msg)
			print(f"* Welcome {self.nick}")
		except:
			print('Could not connect to server')

############################################ CLI FUNCTIONS ################################################

	def read_file(self, file):
		with open(str(file)) as f:
			self.con.send('\n'.encode("UTF-8"))
			lines = f.readlines() 
			for line in lines:
				self.con.send(line.encode("UTF-8"))
			self.con.send('\n'.encode("UTF-8"))
	
	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')
	
	def display_help(self):
		pass

############################################################################################################

	def send_msg(self):
		while True:
			try:
				msg = input("") # input needs to be blank for formatting

				# cmd line functions
				if msg == 'EXIT()':
					self.con.close()
					os._exit(1)
				elif msg == 'READ()': # have to hit enter twice. Why?
					filename = input("Path to File: ")
					try:
						self.read_file(filename)
					except Exception as e:
						print(e)
						continue
				elif msg == 'CLS()':
					self.clear()
				elif msg == 'HELP()':
					ux.print_client_help()
				else:
					self.con.send(f"[{self.nick}] {msg}".encode("UTF-8"))

			except:
				print("connection failed")
				break
			
	def recv_msg(self):

		#thread to send messages if message is typed
		self.thread(self.send_msg)

		while True:
			
			try:
				msg = self.con.recv(2048).decode("UTF-8")
				if msg == "NICK":
					self.con.send(self.nick.encode("UTF-8"))
				else:
					print(msg)
			
			except Exception as e:
				print(e)
				break

	#print info
	def get_constants(self, pref):
		return dict((getattr(self.con,n), n) for n in dir(self.con) if n.startswith(pref))

	def __repr__(self):
		
		try:
			# object attributes for socket object, easier to see if strings are in the attribute
			# since actual attribute name is long
			families = str(self.get_constants('AF_'))
			types = str(self.get_constants('SOCK_'))
			protocols = str(self.get_constants("IPPROTO_"))

			structure = f"family: {families}, type: {types}, ip: {self.ip}, port: {self.port}, protocol: {protocols}"
			return structure
		
		except:
			print('socket not AF_INET and/or TCP')






class Server(Client):
	def __init__(self, ip, port, users=None):
		super().__init__(ip, port)

		# Not good to put a mutable object in init, could cause problems with different versions 
		if users == None:
			self.users = {}
		else:
			self.users = users
	
	def listen(self):
		self.con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse addr if con reopened
		self.con.bind((self.ip, self.port))
		self.con.listen(5)
	
	def accept(self):
		self.con.accept()
	
	def broadcast(self, msg, client_sock=None):
		for client in self.users.keys():
			if client != client_sock:
				client.send(msg.encode("UTF-8"))

	def handle_client(self, client_sock, nick):
		while True:
			msg = client_sock.recv(2048).decode('UTF-8')
			self.broadcast(msg, client_sock)
			print(msg)
			if not msg:
				print(f"{nick} has left the chat")
				for key, value in self.users.items():
					if value == nick:
						del self.users[key]
						break
				print(f"users: {[user for user in self.users.values()]}")
				client_sock.close()
				break	
	
############################################ CLI FUNCTIONS ################################################

	def log(self):
		pass

	def bc(self, name):
		for key, value in self.users.items():
			if name == value:
				personal = input("message: ")
				key.send(f"[SERVER] {personal}".encode("UTF-8"))

	def read_file(self, file):
		with open(str(file)) as f:
			self.broadcast("\n")
			lines = f.readlines() 
			for line in lines:
				self.broadcast(line)
			self.broadcast("\n")
	def ls(self):
		user_table = Table(title="Users")
		user_table.add_column("Username")
		user_table.add_column("Connection")
					
		socks = [sock for sock in self.users.keys()]
		users = [user for user in self.users.values()]
		for user, sock in zip(users, socks):
			user_table.add_row(user, str(sock))
		self.console.print(user_table)
	
	# Kick function still buggy
	def kick(self, user):
		try:
			for key, value in self.users.items():
				if user == value:
					key.send("You have been kicked from server.".encode("UTF-8"))
					key.close()
		except Exception as e:
			print(e)

##########################################################################################################

	def cmd_line_functions(self):
		while True:
			try:
				msg = input("") 
				
				if msg == 'EXIT()':
					self.con.close()
					os._exit(1)
				elif msg == 'READ()':
					filename = input("Path to File: ")
					try:
						self.read_file(filename)
					except Exception as e:
						print(e)
						continue
				if msg == 'CLS()':
					self.clear()
				elif msg == 'HELP()':
					ux.print_server_help()
				elif msg == 'LS()':
					self.ls()
				elif msg == 'BC()':
					try:
						name = input("User to send message: ")
						self.bc(name)
					except Exception as e:
						print(e)
						continue
				elif msg == "KICK()":
					user = input("Username to kick: ")
					self.kick(user)
				elif msg == 'LOG()':
					pass
				else:
					self.broadcast(f"[SERVER] {msg}")
			except Exception as e:
				print(e)
				break

	def start(self):

		# prints help table at startup. Imported from ux module 
		ux.print_server_help()

		while True:
			try:
				client_sock, addr = self.con.accept()
				client_sock.send("NICK".encode("UTF-8"))
				nick = client_sock.recv(2048).decode("UTF-8")
				self.users[client_sock] = nick
				self.broadcast(f"\n{nick} has joined the chat!\n", client_sock)

				# Turn this into a cmd line server function 
				print(f"users: {[user for user in self.users.values()]}")

				# Start threads
				self.thread(self.handle_client, (client_sock, nick))
				self.thread(self.cmd_line_functions)

			#Shutdown server of ctrl-c	
			except KeyboardInterrupt:
				print('[GOODBYE]')
				self.con.close()
				os._exit(1)





