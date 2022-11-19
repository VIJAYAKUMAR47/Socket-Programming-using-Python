import socket

s = socket.socket()
print("Socket successfully created")


port = 8000
s.bind(('localhost', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print(type(name))
    print('Got connection from', addr, name)
    c.send(bytes('Hi Client', 'utf-8'))
    c.close()
