import pytest
#https://pypi.org/project/pytest-socket/
#Testing functionality for base client class

def test_sanity(socket):
	assert socket.ip == '127.0.0.1'

def test_IPv(socket):
	assert str(socket.con.family) == "AddressFamily.AF_INET"


def test_TCP(socket):
	assert str(socket.con.type) == "SocketKind.SOCK_STREAM"

def test_recv(socket):
	pass

def test_shutdown(socket):
	pass