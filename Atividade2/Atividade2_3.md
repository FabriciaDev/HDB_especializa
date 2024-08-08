Atividade 2.3 - Criar um alerta
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Vamos criar um alerta enviar uma notificação cada vez que o comando adduser for utilizado. Isso pode nos dar um controle, por exemplo, para usuários criados sem o consentimento do administrador do sistema.

## Digite a consulta para encontrar todas as instâncias em que o comando adduser foi usado e registrado no arquivo "/var/log/auth.log":


    index=* sourcetype="linux_secure" source="/var/log/auth.log" "adduser"
    | rex field=_raw "adduser (?<username>.*)" 
    | table _time, host, source, username
## Para criar um alerta, selecione "Save As" e, em seguida, selecione "Alert".
##Volte ao terminal, e digite o comando para criar um novo usuário, com senha 123.

$ sudo adduser exemplo2

## Os dados pessoais como nome e telefone podem ser deixados em branco, basta apertar a tecla "Enter".

## >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

## Na tela inicial do Splunk, clique na opção "Activity" na barra superior, depois em "Triggered Alerts". Veja que um alerta foi disparado após o uso do comando adduser.
