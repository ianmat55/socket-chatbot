import pytest
import base_socket as base

ip = '127.0.0.1' #localhost
port = 6500

#set up and tear down for test runs
@pytest.fixture
def socket():
	s = base.Socket()
	return s

@pytest.fixture
def server():
	pass