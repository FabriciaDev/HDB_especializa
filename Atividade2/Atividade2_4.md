# Atividade 2.4 - Criar um Dashboard
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

##  A partir da tela inicial, clique em "Search & Reporting" localizado no painel lateral esquerdo, e digite a query a seguir.

source="/var/log/auth.log" host="ip-192-168-98-10" sourcetype="linux_secure"

## Para adicionar essa query em um Painel, localize a opção "Save As", e depois clique em "New Dashboard".

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk14.PNG">
</p>

Dashboard Title: Painel de monitoramento

Permissions: Private

How do you want to build your dashboard?: Classic Dashboards

Panel Title: Monitoramento

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk15.PNG">
</p>

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk16.PNG">
</p>

## >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

### Clique em "Save to Dashboard", e depois em "View Dashboard".

Você montou com sucesso o seu painel, faça aqui a captura de tela.

Agora, você pode acompanhar diretamente os registros do sistema através do painel "Dashboards". Tudo que você precisa fazer é selecionar no seu painel as opções que você quer monitorar, como por exemplo, os registros do servidor. A partir de agora, você pode monitorar quantos arquivos do seu servidor quiser, basta adicioná-los ao seu painel.
