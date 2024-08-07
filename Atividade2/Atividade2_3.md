Atividade 2.3 - Criar um alerta
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Vamos criar um alerta enviar uma notificação cada vez que o comando adduser for utilizado. Isso pode nos dar um controle, por exemplo, para usuários criados sem o consentimento do administrador do sistema.

Digite a consulta para encontrar todas as instâncias em que o comando adduser foi usado e registrado no arquivo "/var/log/auth.log":


    index=* sourcetype="linux_secure" source="/var/log/auth.log" "adduser"
    | rex field=_raw "adduser (?<username>.*)" 
    | table _time, host, source, username
    Para criar um alerta, selecione "Save As" e, em seguida, selecione "Alert".
