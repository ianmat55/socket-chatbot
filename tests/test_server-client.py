# Test module for client server connnection


def test_sanity(server):
	assert server.con != None 


class Test_Sockets:

	def test_connection(self, server, client):
		pass