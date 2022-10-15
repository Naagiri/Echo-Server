import socket 
import pickle

print('Server launched')

sock = socket.socket()
sock.bind(('', 9090))

print('Start listening the port')
sock.listen(1)

print('Connecting the client')

conn, addr = sock.accept()

print('Getting data from client')

msg = conn.recv(1024).decode()
print(msg)


print('Sending data to client')
conn.send(msg.encode())

print('Turning off the client')
conn.close()

print('Server turned off')
