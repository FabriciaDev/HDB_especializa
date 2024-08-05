from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   print('_host_ a ser escaneado: 45.33.32.156')
   print('Pressione enter')
   input()
   target = '45.33.32.156'
   t_IP = gethostbyname(target)
   print ('Iniciando varredura no _host_: ', t_IP)
   
   for i in range(70, 81):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Porta %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)
