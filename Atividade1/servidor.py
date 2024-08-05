import socket
def Main():
   _host_ = socket.gethostname()
   port = 12345
   serversocket = socket.socket()
   serversocket.bind((_host_,port))
   serversocket.listen(1)
   print('socket esta na escuta')
   
   while True:
      conn,addr = serversocket.accept()
      print("Recebido conexao de %s" % str(addr))
      msg = 'Conexao estabelecida'+ "\r\n"
      conn.send(msg.encode('ascii'))
      conn.close()
if __name__ == '__main__':
   Main()
