import pytest
#https://pypi.org/project/pytest-socket/

#Testing functionality for base client class (unit test)
class Test_Base:
	def test_sanity(self, socket):
		assert socket.ip == '127.0.0.1'

	def test_IPv(self, socket):
		assert 'AF_INET' in str(socket.con.family)

	def test_TCP(self, socket):
		assert 'SOCK_STREAM' in str(socket.con.type)
	
	def test_connection(self, server, socket):
		server.listen()
		socket.connect()
		client_con, addr = server.con.accept()

		assert client_con != None and addr != None
			

