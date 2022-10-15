import socket
import pickle

sock = socket.socket()
print('Connecting to server')
sock.connect(('localhost', 9090))

print("Sending data to server")

msg = str(input('Enter message: '))
sock.send(msg.encode())


print('Getting data from server')
print(sock.recv(1024).decode())

print('Disconnecting from server')
sock.close()
