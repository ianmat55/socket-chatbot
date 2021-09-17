from base_socket import Client 
import threading

port = 6500

def main():
	ip_enter = input("Enter ip ('local' for localhost): ")
	if ip_enter == 'local':
		ip = '127.0.0.1'
	else: ip = ip_enter
	user = input('what is your name? ')
	client = Client(ip, port, user)
	client.connect()
	client.recv_msg()
	# client.thread(client.recv_msg)
	# client.read_file('texts/poem.txt')

if __name__ == '__main__':
	main()