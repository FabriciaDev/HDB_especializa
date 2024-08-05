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

!https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk1.PNG
