import pytest
#https://pypi.org/project/pytest-socket/

#Testing functionality for base client class (unit test)
class Test_Base:
	def test_sanity(self, socket):
		assert socket.ip == '127.0.0.1'

	def test_IPv(self, socket):
		assert str(socket.con.family) == 'AddressFamily.AF_INET'

	def test_TCP(self, socket):
		assert str(socket.con.type) == 'SocketKind.SOCK_STREAM'
	
	def test_connection(self, server, socket):
		server.listen()
		socket.connect()
		client_con, addr = server.con.accept()

		assert client_con != None and addr != None
	
	def test_message(self, server, socket):
		server.listen()
		socket.connect()
		while True:
			c_message = "TESTING"
			socket.send_msg(c_message)
			client_con, addr = server.con.accept()

			if client_con:
				s_message = server.recv_msg(client_con).decode("UTF-8")
				break

		assert s_message == c_message 
			

#testing server
class Test_Server:
	def test_server_start(self):
		pass

	def test_client_connect(self):
		pass

	def test_end(self):
		pass

	def test_transcribe(self):
		pass

#testing client
class Test_Client:
	def test_connect(self):
		pass

	def test_declare_name(self):
		pass

	def test_read_script(self):
		pass

	def test_send(self):
		pass

	def test_disconnect(self):
		pass