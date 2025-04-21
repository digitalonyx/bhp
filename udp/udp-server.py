import socket
import threading

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to a local address and port
server_address = ('127.0.0.1', 9997)
sock.bind(server_address)

print(f'[*] Listening on {server_address[0]}:{server_address[1]}')

while True:
    # Receive data
    data, client_address = sock.recvfrom(4096)
    print(f"Received  {data.decode()} from {client_address}")

    # Send a response
    response = b"Message received!"
    sock.sendto(response, client_address)