from base_socket import Client 
import threading

ip = '127.0.0.1'
port = 6500

def main():
	user = input('what is your name? ')
	client = Client(ip, port, user)
	client.connect(user)

	client.thread(client.recv_msg)
	# client.read_file('texts/poem.txt')

if __name__ == '__main__':
	main()