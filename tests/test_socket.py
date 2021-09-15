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
			

#testing functionality of multithreaded socket (integration test)
class Test_thread:
	pass

#testing romeo juliet script (system test)
class Test_script:
	pass