# Atividade 2.2 - Monitorar relatórios de fonte de dados

Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

A partir da tela inicial do Splunk, você pode visualizar os dados de autenticação de usuários armazenados no arquivo /var/log/auth.log. Isso pode ser útil, por exemplo, para verificar se aconteceu algum login utilizando uma credencial existente, mas que não foi feito pelo usuário de fato (o que pode indicar um vazamento de usuário e senha), ou para verificar se aconteceu login utilizando outras credenciais que não estavam anteriormente cadastradas pelo administrador do sistema.

### Na barra lateral esquerda, clique em "Search & Reporting".

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk10.PNG">
</p>

Na barra "Search", digite a seguinte Query (consulta):

Copy
source="/var/log/auth.log" host="ip-192-168-98-10" sourcetype="linux_secure"
Obs.: Você deve trocar o valor do campo host, caso o hostname do seu sistema operacional seja diferente do que está sendo considerado aqui. Para verificar, basta digitar no terminal o comando:

Copy
$ hostname
Podemos também verificar todas as tentativas de login no Splunk. Para verificar tentativas de login que falharam, incluindo o nome de usuário digitado, digite a seguinte sintaxe de consulta na barra "Search":

Copy
index=_audit sourcetype = audittrail action="login attempt" info=failed
Já para verificar as tentativas bem sucedidas, digite:

Copy
index=_audit sourcetype = audittrail action="login attempt" info=succeeded
Para visualizar todas as entradas de dados, vá para "Settings→Data→Data Inputs". Em seguida, clique no tipo que deseja visualizar, por exemplo, "Files & Directories".

É possível criar uma consulta SPL para verificar todos os usuários criados de forma específica com a utilização do comando adduser, que geralmente registra uma entrada em /var/log/auth.log. Para encontrar todas as instâncias em que o comando adduser foi usado e registrado neste arquivo, você pode usar o seguinte comando SPL:

Copy
index=* sourcetype="linux_secure" source="/var/log/auth.log" "adduser"
| rex field=_raw "adduser (?<username>.*)" 
| table _time, host, source, username
Esta consulta pesquisa em todos os índices (index=*) para logs sourcetype="linux_secure" (que definimos na atividade 1), que vêm do arquivo "/var/log/auth.log" (source="/var/log/auth.log"), contendo o termo "adduser".

O comando rex é uma expressão regular que procura pelo comando adduser seguido de algum texto. Se a entrada do adduser em /var/log/auth.log incluir sempre o nome do usuário, então essa expressão regular irá capturar esse nome do usuário e atribuí-lo ao campo username.

O comando table formata a saída para ser uma tabela com as colunas tempo (_time), host, source e username.

O comando adduser pode ser usado para adicionar um novo usuário. A criação de um novo usuário criará uma entrada no arquivo /var/log/auth.log. Faça um teste, digite no terminal:

Copy
$ sudo /usr/sbin/adduser exemplo
Defina uma senha fácil de memorizar, por exemplo, 123. Digite novamente a query do item 2 acima, e veja que a inclusão do novo usuário foi registrada. A alteração da senha do usuário recém criado também é visível no log.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Você poderá ver o registro do evento de criação do novo usuário ao repetir a query do passo 2 no Splunk.

Copy
source="/var/log/auth.log" host="ip-192-168-98-10" sourcetype="linux_secure"
