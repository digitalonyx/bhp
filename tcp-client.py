import socket

target_host = "0.0.0.0"
target_port = 9998

# crate a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
#client.send(b"GET /HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")

# send some data
client.send(b"AAABBBCCC")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
