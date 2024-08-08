Atividade 2.3 - Criar um alerta
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Vamos criar um alerta enviar uma notificação cada vez que o comando adduser for utilizado. Isso pode nos dar um controle, por exemplo, para usuários criados sem o consentimento do administrador do sistema.

### Digite a consulta para encontrar todas as instâncias em que o comando adduser foi usado e registrado no arquivo "/var/log/auth.log":


    index=* sourcetype="linux_secure" source="/var/log/auth.log" "adduser"
    | rex field=_raw "adduser (?<username>.*)" 
    | table _time, host, source, username
### Para criar um alerta, selecione "Save As" e, em seguida, selecione "Alert".
<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk11.PNG">
</p>

### Será apresentada a tela onde você poderá inserir detalhes adicionais.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/splunk12.PNG">
</p>

Title: Uso do adduser.

Description: Cada vez que o comando adduser for utilizado.

Permissions: As opções existentes são Privadas e Compartilhadas no aplicativo. Privado indica que somente você tem permissão para visualizar e editar o alerta, não é visível para outros usuários. Compartilhado no aplicativo indica que o alerta está disponível para outros usuários no aplicativo de pesquisa e geração de relatórios. O alerta fica visível para outros usuários neste contexto. Dependendo de suas permissões, outros usuários podem editar o painel. Deixe maracado a opção Private.

Alert type: As opções disponíveis são "Agendado" e "Tempo real" e abaixo estão os detalhes. No nosso caso, como iremos gerar um único evento de teste, marque a opção Real-time.

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/alerta1.PNG">
</p>

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade2/alerta2.PNG">
</p>

Expires: 60 minute(s).

Trigger alert when: Per-Result.

Throttle (Limitador): No nosso caso, como o alerta deverá ser disparado uma única vez quando uma condição específica for atendida, não há necessidade de marcar a caixa de seleção.

Se você programou pesquisas que são executadas com regularidade e não quer ser notificado a cada vez que os resultados são gerados, ajuste os controles de limitação para que o alerta seja suprimido por um intervalo de tempo mais longo.

A opção "Throttle" indica que as notificações de alerta devem ser suprimidas pelo período de tempo estabelecido e, caso tenha escolhido disparar para cada resultado, por quaisquer valores de campo especificados. O período de tempo padrão é de 60 segundos, mas você pode personalizá-lo conforme suas necessidades. Essas configurações vão ajudar a evitar que sua caixa de entrada de email fique abarrotada de emails de notificação de alerta.

Trigger Actions: Marque a opção Add to Triggered Alerts, com a severidade Medium.

Os campos nesta seção são autoexplicativos, mas observe que podemos usar tokens no assunto e no corpo do e-mail para adicionar especificidade ao alerta. Por exemplo, os campos de assunto e corpo são pré-preenchidos com texto que usa o token $name$, que será substituído pelo nome da pesquisa quando o alerta for enviado.

Depois de salvar o alerta, você verá a tela de alterações nas permissões clicando em "Permissions". Pode deixar marcado a opção Owner, e clicar em "Save".
### Volte ao terminal, e digite o comando para criar um novo usuário, com senha 123.

$ sudo adduser exemplo2

## Os dados pessoais como nome e telefone podem ser deixados em branco, basta apertar a tecla "Enter".

## >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

## Na tela inicial do Splunk, clique na opção "Activity" na barra superior, depois em "Triggered Alerts". Veja que um alerta foi disparado após o uso do comando adduser.
