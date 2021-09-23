from base_socket import Client, Server
import pytest, time, threading, socket, os


ip = '127.0.0.1'
port = 6500
user = "DUMMY"


# Test module for client server connection. If it exists
def test_ServerInit(server):
	assert server.con != None

def test_ServerStart(server):
	server_thread = threading.Thread(target=server.start)
	server_thread.start()
	assert server.con != None

def test_ServerAccept(server):

	client_dummy = Client(ip,port,user)

	server_thread = threading.Thread(target=server.start)
	server_thread.start()
	client_dummy.connect()

	assert server.con != None






	

		



	

