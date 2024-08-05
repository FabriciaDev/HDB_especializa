import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_host_ = socket.gethostname()
port = 12345

s.connect((_host_, port))
msg = s.recv(1024)

s.close()
print (msg.decode('ascii'))
