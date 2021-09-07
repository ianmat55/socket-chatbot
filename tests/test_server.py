import pytest
from socket_tutorial.server import server_init

#settings
@pytest.fixture
def client():
	settings = {
	'server': '127.0.0.1', 
	'port':  65432 
	}

	return settings

def test_sanity(client):
	assert client['server'] == '127.0.0.1' and client['port'] == 65432

#does the server run

#can clients connect to it

#can it recieve messages

#closing the server

#multiple clients

#distinguish client messages

#list clients

#boot a client that says something 

