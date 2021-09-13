import pytest
from threading import server_thread, client_thread

@pytest.fixture()
def myserver(server_thread):
	server_thread.main()
	
