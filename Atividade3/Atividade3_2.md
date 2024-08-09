# Atividade 3.2 - Análise de arquivos com o Zeek
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Com o File Analysis Framework, o Zeek pode executar diversas tarefas relacionadas à segurança e forense de arquivos, incluindo Hashing automático de arquivos, Identificação de arquivos maliciosos, Extração de arquivos, Análise do tipo de arquivo, Análise de Entropia, Registro de todos os arquivos vistos na rede.

### No arquivo /opt/zeek/share/zeek/site/local.zeek, as linhas relevantes para carregar as funcionalidades de hashing de arquivo e as pesquisas do Malware Hash Registry do Team Cymru geralmente se parecem com o seguinte:

    sudo nano /opt/zeek/share/zeek/site/local.zeek

# .
    (...)

    # Enable MD5 and SHA1 hashing for all files.
    @load frameworks/files/_hash_-all-files

    # Detect SHA1 sums in Team Cymru's _Malware_ Hash Registry.
    @load frameworks/files/detect-MHR
O caractere @ na frente do comando "load" indica uma instrução Zeek para carregar um script ou módulo. Para sair do nano, pressione "Ctrl + X".

A função de hash SHA256 não está habilitada automaticamente. Vamos resolver isso criando um pequeno script Zeek.

### Crie um novo arquivo no diretório /opt/zeek/share/zeek/site com o nome hash_sha256.zeek, conforme as linhas de código a seguir:

    sudo nano /opt/zeek/share/zeek/site/hash_sha256.zeek

linhas 

    ##! Realiza o hashing SHA256 em todos os arquivos.
    @load base/files/hash
    event file_new(f: fa_file)
      {
      Files::add_analyzer(f, Files::ANALYZER_SHA256);
      }

### Para salvar pressione a combinação de teclas "Ctrl + O", depois "Enter". Para sair do nano, pressione "Ctrl + X".

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

### Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

    export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"

### Edite o arquivo /opt/zeek/share/zeek/site/local.zeek, adicionando as linhas a seguir após a última linha do arquivo. Faça a captura de tela desse arquivo editado.

    sudo nano /opt/zeek/share/zeek/site/local.zeek

linhas

    # Inclui o _hash_ SHA256 para os arquivos
    @load hash_sha256
    Novamente, salvar com "Ctrl + O", depois "Enter". Para sair, pressionar "Ctrl + X".

### Pare o Zeek com o comando:

    sudo /opt/zeek/bin/zeekctl stop

### Aplique as novas configurações e inicie o Zeek utilizando o comando:

    sudo /opt/zeek/bin/zeekctl deploy
