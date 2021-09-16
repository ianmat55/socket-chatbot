from base_socket import Server

ip = '127.0.0.1'
port = 6500

def main():
	server = Server(ip, port)
	server.listen()
	server.start()

if __name__ == '__main__':
	main()

