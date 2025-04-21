import socket

# create a socket object 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server address 
server_address = ('127.0.0.1', 9997)

# message to send
message = b'Hello'

try:
    # send data
    print(f'Sending: {message.decode()}')
    sock.sendto(message, server_address)

    # Set a timeout so it doesn't hang 
    sock.settimeout(2.0)

    # Receive response
    data, server = sock.recvfrom(4096)
    print(f'Received: {data.decode()}')

except socket.timeout:
    print("No response from server (timeout).")

finally:
    sock.close()