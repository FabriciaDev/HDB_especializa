# Atividade 1.1 - Coleta de informações
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Nesta atividade, vamos construir um servidor de echo usando a biblioteca Socket, disponível no Python. Isso nos permitirá ecoar dados na porta UDP. Ferramentas como o Nmap vão conseguir encontrar facilmente as portas abertas, então podemos usar isso a nosso favor para tornar o sistema mais seguro. O servidor não apenas escuta vários clientes e recebe as informações, mas também retorna as mensagens para o cliente.

Antes de continuarmos, é importante lembrar que um soquete de rede é um ponto final dentro de um nó em uma rede de computadores, que usamos principalmente para enviar ou receber dados. É uma representação na pilha de protocolos e também funciona como um recurso do sistema.

### Vamos abrir o editor de texto "nano" no terminal:

$ nano servidor.py

### Agora escreva o seguinte código para o servidor:

https://github.com/FabriciaDev/HDB_especializa/blob/main/servidor.py

No programa acima, temos o método socket.bind(). Pense nele como o ponto de amarração do nosso servidor a um IP e porta específicos. É ali que ele vai ficar ouvindo as solicitações que chegam naquele IP e porta.

Em seguida, temos o método socket.listen(), que coloca nosso servidor em modo de escuta, pronto para ouvir as solicitações dos clientes.

Agora, imagine que você passa o número 4 como argumento para o método socket.listen(). Isso significa que nosso servidor vai manter 4 conexões em fila de espera. Se um 5º cliente tentar estabelecer conexão enquanto o servidor está ocupado, ele não conseguirá.

Para enviar uma mensagem ao cliente, usamos o método socket.send().

Por fim, temos os métodos socket.accept() e socket.close(), que são usados para iniciar e encerrar a conexão, respectivamente.

### Vamos para o programa de soquete do lado do cliente. Abra o editor de texto no terminal:

$ nano cliente.py

### Insira o seguinte código:

https://github.com/FabriciaDev/HDB_especializa/blob/main/cliente.py

Nesse código, precisamos criamos um objeto de soquete.

Depois, conectamos à porta onde nosso servidor está em ação - no nosso caso, é a porta 12345.

A partir daí, estabelecemos uma conexão com o servidor usando o método socket.connect().

Uma vez que a conexão está estabelecida, o cliente pode receber a mensagem do servidor através do método socket.recv().

E para finalizar, o método socket.close() é utilizado para encerrar o cliente.

### Execute primeiramente o código do Socket servidor:

$ python3 servidor.py

### A saída será:

socket esta na escuta

### Deixe o código do servidor em execução na janela do terminal. Abra uma nova janela de terminal, e execute agora o cliente:

$ python3 cliente.py

Conexao Estabelecida
### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Volte para a janela de terminal do servidor e faça a captura de tela da saída na tela.

