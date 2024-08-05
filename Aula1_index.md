Aula 01
Atividade Prática - Ameaças Cibernéticas (Cyber Threats) e Metodologia de Cadeia de Eliminação (Kill Chain Methodology)
Vamos começar as nossas atividades conhecendo algumas ferramentas que podem ser úteis nas atividades da Resposta a Incidentes relacionadas a uma invasão cibernética.

Primeiro, vamos entender a fase de coleta de informações. Essa é a hora em que você precisa se tornar um "expert" sobre o cliente - saber tudo mesmo, até o software que está rodando no sistema deles. Além disso, é necessário conhecer as portas que estão ouvindo - pode ser que tenham mais abertas do que deveriam, e isso é um problema! Imagine que uma empresa contratou você para um teste de invasão interno. Você precisa conhecer o endereço IP do controlador de domínio deles.

Essa etapa, a coleta de informações, também chamada de recolhimento de inteligência ou reconhecimento, é onde tudo começa. Dali, partimos para os testes, que podem ser manuais ou automatizados, focados na rede, nos aplicativos, ou até mesmo físicos. E o último passo, a cereja do bolo: a engenharia social.

Instruções para entrega da Atividade Prática
Leia com atenção!
No final deste módulo você deve submeter em um ÚNICO arquivo PDF as seguintes capturas de tela:

Atividade 1.1: passo 7.

Atividade 1.2: passo 3.

Atividade 1.3: passo 2.

Atividade 1.4: passo 3.

Atividade 1.5: passo 3.

O arquivo deverá conter:

O seu nome completo;

O título de cada atividade, que irá conter a resposta de cada passo identificada pelo seu respectivo número;

Caso a resposta seja uma captura de tela do prompt em tela, substitua o nome de usuário no terminal para o seu nome e sobrenome, configurados como um alias (apelido), juntamente com a data e hora atuais. Por exemplo, se o se nome é "Meu Nome", no início da tarefa, execute o comando:

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Obs.: Você terá que digitar o comando acima cada vez que acessar o terminal do Linux.

A captura de tela do prompt deverá mostrar o comando digitado e a saída (output) deste comando. Caso seja necessário, enviar uma captura de tela contendo o comando, e outra captura de tela contendo a saída em tela, por exemplo, quando o texto da saída suprimir o texto do comando digitado.

Atividade 1.1 - Coleta de informações
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Nesta atividade, vamos construir um servidor de echo usando a biblioteca Socket, disponível no Python. Isso nos permitirá ecoar dados na porta UDP. Ferramentas como o Nmap vão conseguir encontrar facilmente as portas abertas, então podemos usar isso a nosso favor para tornar o sistema mais seguro. O servidor não apenas escuta vários clientes e recebe as informações, mas também retorna as mensagens para o cliente.

Antes de continuarmos, é importante lembrar que um soquete de rede é um ponto final dentro de um nó em uma rede de computadores, que usamos principalmente para enviar ou receber dados. É uma representação na pilha de protocolos e também funciona como um recurso do sistema.

Vamos abrir o editor de texto "nano" no terminal:

Copy
$ nano servidor.py
Agora escreva o seguinte código para o servidor:

Copy
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
No programa acima, temos o método socket.bind(). Pense nele como o ponto de amarração do nosso servidor a um IP e porta específicos. É ali que ele vai ficar ouvindo as solicitações que chegam naquele IP e porta.

Em seguida, temos o método socket.listen(), que coloca nosso servidor em modo de escuta, pronto para ouvir as solicitações dos clientes.

Agora, imagine que você passa o número 4 como argumento para o método socket.listen(). Isso significa que nosso servidor vai manter 4 conexões em fila de espera. Se um 5º cliente tentar estabelecer conexão enquanto o servidor está ocupado, ele não conseguirá.

Para enviar uma mensagem ao cliente, usamos o método socket.send().

Por fim, temos os métodos socket.accept() e socket.close(), que são usados para iniciar e encerrar a conexão, respectivamente.

Vamos para o programa de soquete do lado do cliente. Abra o editor de texto no terminal:

Copy
$ nano cliente.py
Insira o seguinte código:

Copy
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_host_ = socket.gethostname()
port = 12345

s.connect((_host_, port))
msg = s.recv(1024)

s.close()
print (msg.decode('ascii'))
Nesse código, precisamos criamos um objeto de soquete.

Depois, conectamos à porta onde nosso servidor está em ação - no nosso caso, é a porta 12345.

A partir daí, estabelecemos uma conexão com o servidor usando o método socket.connect().

Uma vez que a conexão está estabelecida, o cliente pode receber a mensagem do servidor através do método socket.recv().

E para finalizar, o método socket.close() é utilizado para encerrar o cliente.

Execute primeiramente o código do Socket servidor:

Copy
$ python3 servidor.py
A saída será:

Copy
socket esta na escuta
Deixe o código do servidor em execução na janela do terminal. Abra uma nova janela de terminal, e execute agora o cliente:

Copy
$ python3 cliente.py

Conexao Estabelecida
>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Volte para a janela de terminal do servidor e faça a captura de tela da saída na tela.

Atividade 1.2 - Port Scanner usando Socket
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

A varredura de portas ajuda a descobrir quais portas estão abertas em um determinado host. Ela pode ser ajustada de acordo com as nossas necessidades, para coletar o máximo de informações possíveis do sistema alvo.

A varredura de porta pode fornecer o seguinte tipo de informação:

Dados sobre portas abertas.

Informações sobre os serviços rodando em cada porta.

Detalhes sobre o sistema operacional e o endereço MAC do host alvo.

A suíte de protocolos TCP/IP, usada para comunicação na internet, é composta por dois protocolos principais, o TCP e o UDP. Ambos os protocolos têm um total de 65535 portas. É sempre bom fechar as portas desnecessárias do nosso sistema, então temos mais de 65.000 portas para bloquear. Essas 65535 portas podem ser divididas em três faixas:

Sistema ou portas conhecidas: de 0 a 1023

Usuário ou portas registradas: de 1024 a 49151

Portas dinâmicas ou privadas: todas acima de 49151

Vamos usar o conhecimento da atividade 1 para construir um scanner de porta simples utilizando socket.

Vamos abrir o editor de texto "nano" no terminal:

Copy
$ nano atividade2.py
Digite o script em Python a seguir dentro do arquivo de texto:

Copy
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
CUIDADO: A varredura de portas pode ser vista ou interpretada como uma atividade ILEGAL.

Jamais devemos rodar um scanner de porta em qualquer site ou endereço IP sem a permissão explícita e por escrito do dono do servidor ou do computador que está sendo alvo.

A varredura de portas pode ser análoga a ir até a casa de alguém e inspecionar suas portas e janelas. Por isso, é recomendável usar o scanner de porta no host local ou no seu próprio site, se tiver um.

O script acima irá fazer a varredura entre um intervalo de portas (70-81), no host http://scanme.nmap.org/. O criador do nmap, Gordon Lyon, conhecido pelo pseudônimo de Fyodor, criou esse host especialmente para testes de varredura de portas. Esse endereço, quando digitado no navegador, aponta para uma página que traz uma descrição sobre o uso nesse host:

"Olá, bem-vindo ao Scanme.Nmap.Org, um serviço fornecido pelo Nmap Security Scanner Project.

Configuramos esta máquina para ajudar as pessoas a aprender sobre o Nmap e também para testar e garantir que a instalação do Nmap (ou conexão com a Internet) esteja funcionando corretamente. Você está autorizado a escanear esta máquina com o Nmap ou outros scanners de porta. Tente não martelar o servidor com muita força. Algumas verificações por dia são boas, mas não verifique 100 vezes por dia ou use este site para testar sua ferramenta de quebra de senha de força bruta ssh."

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Execute o programa criado:

Copy
$ python3 atividade2.py
O resultado mostrará que, no intervalo de 70 a 81 (conforme especificado no script), esse scanner de porta encontrou uma porta - a 80 - aberta. Faça a captura de tela desse resultado.

Atividade 1.3 - Reconhecimento
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

O reconhecimento é uma etapa essencial na fase inicial do teste de penetração, onde se coleta o máximo possível de informações sobre o alvo. Esta fase inclui a coleta de informações de domínio público, bem como o uso de ferramentas mais sofisticadas para obter mais detalhes sobre o alvo.

Você pode usar desde o Traceroute, até outras ferramentas como recon-ng, DMitry, Maltego. Como estamos trabalhando com Python, vamos dar uma olhada na ferramenta FinalRecon.

O FinalRecon é uma ferramenta de inteligência de código aberto utilizada em projetos de reconhecimento baseados na web. Ela tem o superpoder de detectar e coletar informações úteis sobre domínios alvo de forma automática. A estrutura modular da ferramenta permite expandir seus recursos de reconhecimento. Vamos dar uma olhada nas características dessa poderosa ferramenta.

Informação WHOIS: Essencial para saber quem está por trás de um determinado domínio.

Informações do Cabeçalho: Dá uma visão das respostas HTTP que o servidor fornece.

Registro de Certificado SSL: Mostra detalhes sobre o certificado de segurança do site.

Enumeração DNS: Revela informações sobre os registros DNS do domínio.

Listagem de Subdomínios: Mapeia todos os subdomínios ligados ao domínio principal.

Informações de Rastreamento de Rota: Fornece a rota que os pacotes seguem até o servidor.

Busca no Diretório: Permite encontrar diretórios ocultos ou esquecidos.

Varredura de Portas: Identifica portas abertas que possam ser exploradas.

Rastreamento Web: Analisa o site para identificar conteúdo e links.

Cada um desses recursos de reconhecimento gera um monte de informações valiosas. Para os testadores de penetração, ajuda na identificação de pontos de injeção potenciais nos hosts alvo.

Uma vez instalada, você pode ver como usar a ferramenta digitando:

Copy
$ python3 /opt/FinalRecon/finalrecon.py -h
>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Verifique o certificado SSL. Substitua o endereço https://www.dominio.com por um site bem conhecido, por exemplo, Google ou Cloudflare. Faça a captura de tela do comando digitado contendo a respectiva saída na tela.

Copy
$ python3 /opt/FinalRecon/finalrecon.py --sslinfo https://www.dominio.com
Agora experimente digitar os comandos a seguir um de cada vez, e veja quais são as saídas no terminal. Substitua o endereço https://www.dominio.com por um site bem conhecido, por exemplo, Google ou Cloudflare.

Verificar cabeçalhos:

Copy
$ python3 /opt/FinalRecon/finalrecon.py --headers https://www.dominio.com
Verificar as informações do whois:

Copy
$ python3 /opt/FinalRecon/finalrecon.py --whois  https://www.dominio.com
Alvo de rastreamento:

Copy
$ python3 /opt/FinalRecon/finalrecon.py --crawl https://www.dominio.com
Verificação completa:

Copy
$ python3 /opt/FinalRecon/finalrecon.py --full https://www.dominio.com
Atividade 1.4 - Um pouco sobre varredura
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Ser capaz de fazer uma varredura sem ser detectado é um desafio perfeito para um hacker. No entanto, como especialista em segurança cibernética, sua prioridade deve ser proteger seu próprio sistema. A ética do hacking não é apenas sobre ataque, mas também sobre autodefesa.

Vamos falar um pouco sobre footprinting, algo como "pegadas digitais". Imagine a seguinte situação: você se depara com um endereço IP vindo do Panamá. Se você resolver pesquisar esse endereço IP em um serviço Whois, você pode ficar bem surpreso. Sabe por quê? Muitos dos endereços IP por aí não seguem as melhores práticas de segurança. Não é raro encontrar informações valiosas como endereços completos, contatos, IDs de administradores e muito mais coisas que, na real, não deveriam ser disponibilizadas assim tão facilmente.

A pesquisa Whois pode ser usada para qualquer URL. E tem mais: você pode fazer a ação contrária usando o terminal da sua máquina virtual Linux. Existe um comando bem útil chamado nslookup. É só digitá-lo na linha de comando junto com qualquer extensão de URL, e você recebe o endereço IP correspondente.

Vamos ver como isso funciona. Veja o seguinte comando:

Copy
$ nslookup scanme.nmap.org
Server:         10.0.2.3
Address:        10.0.2.3#53

Non-authoritative answer:
Name:   scanme.nmap.org
Address: 45.33.32.156
Name:   scanme.nmap.org
Address: 2600:3c01::f03c:91ff:fe18:bb2f
O número na segunda linha (#53) indica a porta para um servidor DNS. O anonimato é super importante no mundo do hacking ético. Você pode usar navegadores como o Tor ou alterar as configurações do sistema para manter o anonimato enquanto usa ferramentas de hacking.

E se você tiver um endereço IP? A pesquisa reversa também é bem fácil com o comando nslookup. Vamos tentar isso com o endereço IP de scanme.nmap.org no Linux:

Copy
$ nslookup 45.33.32.156
156.32.33.45.in-addr.arpa       name = scanme.nmap.org.

Authoritative answers can be found from:
32.33.45.in-addr.arpa   nameserver = ns5.linode.com.
32.33.45.in-addr.arpa   nameserver = ns3.linode.com.
32.33.45.in-addr.arpa   nameserver = ns1.linode.com.
32.33.45.in-addr.arpa   nameserver = ns2.linode.com.
32.33.45.in-addr.arpa   nameserver = ns4.linode.com.
A diferença mais uma vez fica por conta do endereço do servidor. Mas tem outra coisa legal aqui:

Copy
156.32.33.45.in-addr.arpa	name = scanme.nmap.org.
O endereço IP de scanme.nmap.org é mostrado na ordem inversa. Bacana, né?

A gente ainda não acabou com a varredura digital. Em alguns casos, quando você se aprofunda mais, pode ver que algumas varreduras podem levar dias para terminar. Por agora, vamos continuar olhando para o scanme.nmap.org e tentar descobrir quantas portas estão abertas lá.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Volte ao Nmap e digite o comando:

Copy
$ nmap scanme.nmap.org -vv
O resultado vai mostrar algumas informações interessantes. Realize a captura de tela do resultado.

Repare na última parte do resultado. Tem uma lista que mostra quantas portas estão abertas. Isso já dá uma ideia do que é uma varredura real.

Atividade 1.5. Outras ferramentas
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Outra ferramenta muito útil disponível para usar junto com o Nmap é o comando curl. Com ele, você pode fazer uma varredura em qualquer endereço IP. Ele fornece ainda mais informações sobre esse IP, como localização, nome da organização, cidade e assim por diante. É um tipo de busca Whois, mas muito mais rica em detalhes. A única limitação é que você pode fazer varredura em apenas 1.000 IPs por dia. Se precisar de uma varredura massiva, vai precisar de uma máquina mais poderosa.

Vamos supor que você queira saber a localização e outras informações sobre o <scanme.nmap.org>. Digite curl ipinfo.io/45.33.32.156 no seu terminal e você recebe o resultado imediatamente.

Copy
$ curl ipinfo.io/45.33.32.156
{
  "ip": "45.33.32.156",
  "hostname": "scanme.nmap.org",
  "city": "Fremont",
  "region": "California",
  "country": "US",
  "loc": "37.5483,-121.9886",
  "org": "AS63949 Akamai Connected Cloud",
  "postal": "94536",
  "timezone": "America/Los_Angeles",
  "readme": "https://ipinfo.io/missingauth"
} 
De uma vez só, você tem tudo: cidade, região, CEP, país e nome da organização. Como você pode ver, o curl é uma ferramenta bem bacana.

Seja grande ou pequena, qualquer organização que esteja digitalmente conectada está sempre sob risco. Como um aspirante a especialista em testes de penetração, você precisa entender isso bem. Existem muitas ferramentas que podem te ajudar nesse trabalho, e uma as delas é o DMitry (Deepmagic Information Gathering Tool). Essa ferramenta coleta o máximo de informações possíveis.

Usar o DMitry é simples. No terminal, você digita:

Copy
$ /bin/dmitry google.com
Ele vai começar a te dar informações como essa:

Copy
//output from running DMitry HostIP:216.58.203.206
HostName:google.com

[...]
Você também pode obter informações sobre os subdomínios.

O DMitry é uma ferramenta bem útil. Ele reúne todas as informações que consegue sobre o host e faz uma varredura nas portas TCP do destino. Faz uma pesquisa Whois muito completa, recolhendo todos os dados possíveis de tempo de atividade, dados do sistema e do servidor.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Se quiser, você ainda pode salvar todas as informações em um arquivo de texto. A partir do seu diretório de login (/home/aluno), é só digitar no terminal:

Copy
$ dmitry -wise -o dmitry.txt google.com
Esse comando vai salvar tudo em um arquivo de texto chamado dmitry.txt no seu diretório de login. Realize a captura de tela do conteúdo do arquivo.

Referências
HackingLoops. How to Automate Web Reconnaissance Using Python Scripts. Disponível em: https://www.hackingloops.com/web-reconnaissance-using-python-scripts/. Acesso em: 12 jul 2023.

Sinha, Sanjib (2018) Beginning Ethical Hacking with Kali Linux. Apress Media LLC.

Tutorials Point. Python Penetration Testing - Quick Guide. Disponível em: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_quick_guide.htm. Acesso em: 12 jul 2023.

Last updated 14 days ago
