import pytest, socket
import base_socket as Socket
import threading

ip = '127.0.0.1' #localhost
port = 6500

#set up and tear down for test runs
#pytest --setup-show to show fixture process in terminal

@pytest.fixture
def client():
	user = "TEST-CLIENT"
	c = Socket.Client(ip,port,user)

	yield c



@pytest.fixture
def server():
	s = Socket.Server(ip,port)
	s.listen()

	yield s




