# Atividade 2.1 - Iniciando a Análise com o Splunk Enterprise
### Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Vamos ver agora um pouco do funcionamento básico do Splunk Enterprise.

Para acessar o Splunk Enterprise, inicie o serviço digitando no terminal:

sudo /opt/splunk/bin/splunk start

##  Caso na primeira execução, apareça a licença do Splunk, role a tela para baixo, e ao aparecer a pergunta "Do you agree with this license? [y/n]", confirme com a tecla "y". Depois, entre com os seguinte dados:

Please enter an administrator username: admin

Please enter a new password: splunk123

Caso sejam necessários, a seguir estão os comandos adicionais para gerenciar (reiniciar ou parar) o daemon splunk.

sudo /opt/splunk/bin/splunk restart

sudo /opt/splunk/bin/splunk stop

### Abra o navegador web, e digite um dos endereços a seguir e aguarde o carregamento da tela de login:

http://127.0.0.1:8000

ou

http://localhost:8000

ou

http://ip-192-168-98-10:8000

## Importante:

### Caso apareça a mensagem de licença expirada, abra o terminal e execute os comandos a seguir para reinstalar o Splunk (NÃO EXECUTAR se a mensagem não aparecer):

    $ sudo su
    # cd /opt
    # ./splunkkillpid.sh
    # ./splunkuninstall.sh
    # ./splunkinstall.sh
    # ./splunkconf.sh
    # exit

### Na tela de login, entre com o nome de usuário e a senha definidos no passo 2 acima.

Username: admin

Password: splunk123

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk1.PNG">
</p>

### Após um login bem-sucedido, você chegará ao console de administração do Splunk mostrado na captura de tela a seguir. Para monitorar um arquivo de log, por exemplo /var/log/auth.log, clique em "Add Data".

Obs.: O arquivo /var/log/auth.log mantém logs de autenticação para logins bem-sucedidos ou com falha e processos de autenticação. Uma das maneiras de habilitá-lo no Debian é instalando o Rsyslog.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk2.PNG">
</p>

### Clique em "Monitor" para adicionar dados de um arquivo.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk3.PNG">
</p>

### Na próxima tela escolha "Files & Directories".

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk4.PNG">
</p>

### Em seguida, configure a instância para monitorar os arquivos e os diretórios em busca de dados. Clique em "Browse" para selecionar a fonte de dados.

Se quiser monitorar todos os objetos em um diretório, selecione o diretório, já se você você quiser monitorar um único arquivo, selecione somente o respectivo arquivo.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk5.PNG">
</p>

### Uma lista de diretórios será mostrada para você, navegue através das setas azuis até o arquivo de log que deseja monitorar (/var/log/auth.log), e clique em "Select" .

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk6.PNG">
</p>

### Depois de selecionar a fonte de dados, selecione "Continuously Monitor" para observar esse arquivo de log e clique em "Next" para definir o tipo de fonte.

### Em seguida, defina o tipo de fonte para sua fonte de dados (caixa de seleção sourcetype). Para nosso arquivo de log de teste (/var/log/auth.log), precisamos selecionar "Operating System→linux_secure"; isso permite que o splunk saiba que o arquivo contém mensagens relacionadas à segurança de um sistema Linux. Em seguida, clique em "Next" para prosseguir. 

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk7.PNG">
</p>

### Você pode, opcionalmente, definir parâmetros de entrada adicionais para esta entrada de dados. Em "App context" , selecione "Search & Reporting". Em seguida, clique em "Review". Após a revisão, clique em "Submit".

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk8.PNG">
</p>

### Agora sua . Clique em "Start Searching" para pesquisar seus dados.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk9.PNG">
</p>

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Você verá a tela de busca "New Search".


