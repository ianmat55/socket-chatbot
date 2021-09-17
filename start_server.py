from base_socket import Server

# ip = '127.0.0.1'
port = 6500

def main():
	ip_enter = input("Enter ip ('local' for localhost): ")
	if ip_enter == 'local':
		ip = '127.0.0.1'
	else: ip = ip_enter
	server = Server(ip, port)
	server.listen()
	server.start()

if __name__ == '__main__':
	main()

