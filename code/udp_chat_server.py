import socket
import sys

# basic udp chat server, facilitates communication between two clients
# messages don't actually get sent through server, only a requested IP address is provided
# used with udp_chat_client.py
# first argument is ip address of the server, second argument is port of the server
if __name__ == '__main__':
	ip_address = str(sys.argv[1])
	port = int(sys.argv[2])

	ip_and_port = (ip_address, port)

	ip_name_dict = {}
	
	chat_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	chat_socket.bind(ip_and_port) # create socket and bind to address


	while True:
		request, client_address = chat_socket.recvfrom(1024) # wait for request
		request = request.decode()

		if request.startswith("login"):
			ip_name_dict[request.split(" ")[1]] = client_address
			chat_socket.sendto("ok".encode(), client_address) # send acknowledgement after adding name to dictionary
		elif request.startswith("chat"):
			chat_socket.sendto(f"ok {str(ip_name_dict[request.split(' ')[1]][0]).encode()} {str(ip_name_dict[request.split(' ')[1]][1]).encode()}".encode(), client_address) # respond with ip address and port number of requested user