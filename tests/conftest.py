import pytest
import base_socket as base
import socket_inherit as s


ip = '127.0.0.1' #localhost
port = 6500

#set up and tear down for test runs
#pytest --setup-show to show fixture process in terminal

@pytest.fixture
def socket():
	s = base.Socket(ip,port)
	yield s

	s.shutdown

@pytest.fixture
def server():
	server = base.Socket(ip,port)
	yield server

	server.shutdown()






