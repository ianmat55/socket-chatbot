import pytest
from socket_tutorial.server import server_init

#settings
@pytest.fixture
def settings():
	settings = {
	'server': '127.0.0.1', 
	'port':  65432 
	}

	return settings

def test_sanity(settings):
	assert settings['server'] == '127.0.0.1' and settings['port'] == 65432

#does the server run
def test_init(settings):
	pass
#can clients connect to it

#can it recieve messages

#closing the server

#multiple clients

#distinguish client messages

#list clients



