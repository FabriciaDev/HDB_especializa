# Atividade 1.2 - Port Scanner usando Socket
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

A varredura de portas ajuda a descobrir quais portas estão abertas em um determinado host. Ela pode ser ajustada de acordo com as nossas necessidades, para coletar o máximo de informações possíveis do sistema alvo.

A varredura de porta pode fornecer o seguinte tipo de informação:

* Dados sobre portas abertas.

* Informações sobre os serviços rodando em cada porta.

* Detalhes sobre o sistema operacional e o endereço MAC do host alvo.

A suíte de protocolos TCP/IP, usada para comunicação na internet, é composta por dois protocolos principais, o TCP e o UDP. Ambos os protocolos têm um total de 65535 portas. É sempre bom fechar as portas desnecessárias do nosso sistema, então temos mais de 65.000 portas para bloquear. Essas 65535 portas podem ser divididas em três faixas:

Sistema ou portas conhecidas: de 0 a 1023

Usuário ou portas registradas: de 1024 a 49151

Portas dinâmicas ou privadas: todas acima de 49151

### Vamos usar o conhecimento da atividade 1 para construir um scanner de porta simples utilizando socket.

### Vamos abrir o editor de texto "nano" no terminal:

$ nano atividade2.py

### Digite o script em Python a seguir dentro do arquivo de texto:

https://github.com/FabriciaDev/HDB_especializa/blob/main/atividade2.py

CUIDADO: A varredura de portas pode ser vista ou interpretada como uma atividade ILEGAL.

Jamais devemos rodar um scanner de porta em qualquer site ou endereço IP sem a permissão explícita e por escrito do dono do servidor ou do computador que está sendo alvo.

A varredura de portas pode ser análoga a ir até a casa de alguém e inspecionar suas portas e janelas. Por isso, é recomendável usar o scanner de porta no host local ou no seu próprio site, se tiver um.

### O script acima irá fazer a varredura entre um intervalo de portas (70-81), no host http://scanme.nmap.org/. O criador do nmap, Gordon Lyon, conhecido pelo pseudônimo de Fyodor, criou esse host especialmente para testes de varredura de portas. Esse endereço, quando digitado no navegador, aponta para uma página que traz uma descrição sobre o uso nesse host:

"Olá, bem-vindo ao Scanme.Nmap.Org, um serviço fornecido pelo Nmap Security Scanner Project.

Configuramos esta máquina para ajudar as pessoas a aprender sobre o Nmap e também para testar e garantir que a instalação do Nmap (ou conexão com a Internet) esteja funcionando corretamente. Você está autorizado a escanear esta máquina com o Nmap ou outros scanners de porta. Tente não martelar o servidor com muita força. Algumas verificações por dia são boas, mas não verifique 100 vezes por dia ou use este site para testar sua ferramenta de quebra de senha de força bruta ssh."

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):


$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"

### Execute o programa criado:

$ python3 atividade2.py

### O resultado mostrará que, no intervalo de 70 a 81 (conforme especificado no script), esse scanner de porta encontrou uma porta - a 80 - aberta. Faça a captura de tela desse resultado.


