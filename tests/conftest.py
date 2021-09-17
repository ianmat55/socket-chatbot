import pytest
import start_client as client
import start_server as server


ip = '127.0.0.1' #localhost
port = 6500

#set up and tear down for test runs
#pytest --setup-show to show fixture process in terminal

@pytest.fixture
def socket():
	c = client.Socket(ip,port)
	yield c

	c.shutdown()

@pytest.fixture
def server():
	s = server.Socket(ip,port)
	yield s

	s.shutdown()






