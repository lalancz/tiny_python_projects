import socket
import threading
import sys

# basic udp chat client, sends username to server which sends back an IP address of the given chatter
# used with udp_chat_server.py
# first argument is ip address of the server, second argument is port of the server

def read_output(chat_socket):
	while True:
		incoming_message = chat_socket.recv(1024)
		incoming_message = incoming_message.decode()

		print(f"Other chatter: {incoming_message}")

def read_input(chat_socket, peer_ip_and_port):
	while True:
		outgoing_message = input("Enter message: ")
		chat_socket.sendto(outgoing_message.encode(), peer_ip_and_port)

if __name__ == '__main__':
	ip_address = str(sys.argv[1])
	port = int(sys.argv[2])

	ip_and_port = (ip_address, port)

	ip_name_dict = {}
	
	chat_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	chat_socket.bind(ip_and_port)

	name = input("Enter your name: ")
	chat_socket.sendto(f"login {name}".encode(), ip_and_port) # sends login request to server

	while True:
		response = chat_socket.recv(1024)
		response = response.decode()
		if response.startswith("ok"): # wait for ok response
			break
	
	peer_name = input("Who do you wish to chat with ('no one' to await a chatter): ")

	if peer_name != "no one":
		chat_socket.sendto(f"chat {peer_name}".encode(), ip_and_port)

		while True: # wait for ok and requested ip address + port number response
			response = chat_socket.recv(1024)
			response = response.decode()
			response = response.split(" ")
			if response[0] == "ok":
				print(response[1][2:-1])
				print(response[2])
				peer_ip_and_port = (str(response[1][2:-1]), int(str(response[2][2:-1]))) # indices get rid of formatting
				print(peer_ip_and_port)
				break
	else:
		incoming_message, address = chat_socket.recvfrom(1024) # wait until someone messages socket
		peer_ip_and_port = address
		print(f"Other chatter: {incoming_message.decode()}")

	read_output_thread = threading.Thread(target=read_output, args=(chat_socket,))

	read_output_thread.daemon = True

	read_output_thread.start() # start thread that prints incoming messages

	while True:
		outgoing_message = input("Enter message: ")
		chat_socket.sendto(outgoing_message.encode(), peer_ip_and_port)  # sends input
