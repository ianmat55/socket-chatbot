from base_socket import Client 
import threading

def main():
	user = input('what is your name? ')
	client = Client('127.0.0.1', 6500, user)
	client.connect()

	client.thread(client.recv_msg)
	client.thread(client.send_msg)
	client.read_file('texts/poem.txt')

	# client.shutdown()

if __name__ == '__main__':
	main()