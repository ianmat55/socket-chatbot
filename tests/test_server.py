from base_socket import Client, Server
import pytest, time, threading, socket, os


ip = '127.0.0.1'
port = 6500
user = "DUMMY"


# Test module for client server connection. If it exists
def test_ServerConnection(server):
	server_thread = threading.Thread(target=server.start)
	server_thread.start()

	dummy_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dummy_client.settimeout(1)
	dummy_client.connect((ip,port))
	
	assert server.con != None
	
	dummy_client.close()
	server.con.close()

		



	

