import pytest, socket
import base_socket as Socket
import threading

ip = '127.0.0.1' #localhost
port = 6500

#set up and tear down for test runs
#pytest --setup-show to show fixture process in terminal

ip = '127.0.0.1'
port = 6500
user = "DUMMY"

@pytest.mark.timeout(2)
@pytest.fixture
def client():
	user = "TEST-CLIENT"
	c = Socket.Client(ip,port,user)

	try:
		yield c

	finally:
		c.con.shutdown(socket.SHUT_RDWR)
		c.con.close()

@pytest.mark.timeout(2)
@pytest.fixture
def server():
	s = Socket.Server(ip,port)

	try:
		yield s

	finally:
		s.con.close()





