import pytest
from base_socket import Client

ip = '127.0.0.1' #localhost
port = 6500

@pytest.fixture
def client():
	Client = Client(ip,port)
	return Client

