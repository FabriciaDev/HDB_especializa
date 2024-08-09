# Atividade 3.1 - Configurando o Zeek
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

O Zeek traz alguns arquivos de configuração, que possuem os seus valores padrão. Não iremos abordar as customizações que podem ser feitas.

### Digite os comandos a seguir no terminal para verificar se os scripts estão ok, e depois para aplicar as configurações e executar o Zeek.

    sudo /opt/zeek/bin/zeekctl check

    sudo /opt/zeek/bin/zeekctl deploy

## >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

### Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

    export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"

Para verificar se o Zeek está sendo executado com sucesso, você pode digitar:

    sudo /opt/zeek/bin/zeekctl status

Espera-se que o status seja "Running".

Observações:

Caso o Zeek não inicialize corretamente, você pode iniciar a inspeção digitando:

    sudo /opt/zeek/bin/zeekctl diag

O Zeek armazena seus logs no diretório /opt/zeek/logs/current/. Você pode verificar se os arquivos de log estão presentes:

    sudo su

    # ls -l /opt/zeek/logs/current/

    # exit

Por exemplo, para verificar o conteúdo do log de conexão Zeek, execute o seguinte comando:

    sudo su
    # tail /opt/zeek/logs/current/conn.log
    # exit
