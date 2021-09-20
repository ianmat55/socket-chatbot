from base_socket import Client, Server
import pytest, time, threading, socket


ip = '127.0.0.1'
port = 6500
user = "DUMMY"


# Test module for client server connection. If it exists
def testServerConnection(server):
	
	time.sleep(.01)

	dummy_client = socket.socket()
	dummy_client.settimeout(1)
	dummy_client.connect((ip,port))
	dummy_client.close()

	assert server.con != None


# Test to see if exception raised if wrong ip is given to client
def testServerFail(server):
	server_thread = threading.Thread(target=server.start)
	server_thread.start()

	time.sleep(.01)

	with pytest.raises(Exception):
		dummy_client = socket.socket()
		dummy_client.settimeout(1)
		dummy_client.connect(('128.0.0.1',port))
		dummy_client.close()
		server_thread.join()
	server.con.close()
	

