# Atividade 2.5 - Casos de uso em Cibersegurança
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Obs.: Estamos considerando o sourcetype="linux_secure" definido na Atividade 1.

### A partir da tela inicial, clique em "Search & Reporting" localizado no painel lateral esquerdo, para digitar as queries a seguir. Alguns resultados podem retornar uma lista vazia, pelo fato de um ou mais eventos ainda não terem ocorrido no sistema.

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

### Monitoramento de Atividades de Root

### As atividades realizadas pelo usuário root (ou qualquer usuário com privilégios de sudo) podem ser de particular interesse durante a análise de incidentes de segurança. O seguinte exemplo de consulta retornará qualquer comando executado pelo usuário root:

index=* sourcetype="linux_secure" source="/var/log/auth.log" "COMMAND=" "USER=root"

| table _time, host, cmd

### Essa consulta pode ser útil para identificar qualquer comportamento suspeito ou não autorizado do usuário root.

### Detecção de Malware

Podemos usar o Splunk para identificar possíveis infecções por malware monitorando os processos em execução no sistema. Podemos, por exemplo, procurar processos que são conhecidos por serem usados por malware ou processos que estão se comportando de maneira suspeita (por exemplo, usando uma alta porcentagem de CPU ou memória).

index=* sourcetype="linux_secure" "process"

| stats count by process_name
| where count > 100

### Essa consulta retornará qualquer processo que tenha sido iniciado mais de 100 vezes, o que pode indicar um comportamento suspeito.

### Monitoramento de Alterações Inesperadas em Arquivos de Sistema Críticos

### O Linux tem vários arquivos e diretórios de sistema críticos que não devem ser alterados com frequência. Uma alteração inesperada nesses arquivos pode ser um indicador de atividade maliciosa. Uma consulta como a seguinte pode ser usada para detectar essas alterações:

index=* sourcetype="linux_secure" source="/var/log/audit/audit.log" "type=CONFIG_CHANGE"

| table _time, host, changes

Essa consulta irá retornar qualquer alteração nos arquivos de configuração do sistema.

### Monitoramento de Conexões de Rede Incomuns

A atividade de rede incomum pode ser um sinal de comprometimento do sistema. Uma consulta como a seguinte pode ser usada para detectar conexões de rede para endereços IP ou portas incomuns:

index=* sourcetype="linux_secure" "type=SYSCALL" and "connect"

| stats count by dest_ip, dest_port
| where count > 100

Essa consulta retorna qualquer conexão para um endereço IP e porta específicos que tenha ocorrido mais de 100 vezes.

### Detecção de Atividades de Escalonamento de Privilégios

A obtenção de privilégios root quando não autorizado é um passo comum em muitos ataques. Uma consulta como a seguinte pode ser usada para detectar tais atividades:

index=* sourcetype="linux_secure" "sudo: pam_unix(sudo:session): session opened for user root"
| table _time, host, user

Essa consulta retorna qualquer instância em que um usuário não root tenha obtido privilégios de root.

### Referências
Hacking Articles. SIEM: Log Monitoring Lab Setup with Splunk. Disponível em: https://www.hackingarticles.in/siem-log-monitoring-lab-setup-with-splunk/. Acesso em: 17 jul 2023.

Service Now. Steps to create an alert in splunk - Support and Troubleshooting. Disponível em: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749544. Acesso em: 17 jul 2023.

Splunk Cheat Sheet: Search and Query Commands. Disponível em: https://www.stationx.net/splunk-cheat-sheet/. Acesso em: 16 jul 2023.

Splunk Community. Disponível em: https://community.splunk.com. Acesso em: 17 jul 2023.

Tecmint. How to Install Splunk Log Analyzer on CentOS 7. Disponível em: https://www.tecmint.com/install-splunk-log-analyzer-on-centos-7/. Acesso em: 17 jul 2023.
