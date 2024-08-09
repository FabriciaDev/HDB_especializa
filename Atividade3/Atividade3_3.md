# Atividade 3.3 - Entendendo os arquivos do tipo log
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Vamos dar uma olhada em seu próprio arquivo do tipo log (conn.log, dns.log, ...), e observar os tipos de arquivos com hash. Aqui no nosso cenário, os arquivos são armaezados no diretório /opt/zeek/logs/current/.

### Visualize o arquivo conn.log acessando:

    $ sudo su
    # cd /opt/zeek/logs/current
    # nano conn.log
    Quando terminar de ver, pressione "Ctrl + X" para sair do Nano. Digite exit para sair do prompt de usuário root.

### Todos os campos do arquivo de log juntos nos ajudam a entender melhor a natureza dos arquivos em trânsito em nossa rede e nos ajudam na detecção e prevenção de atividades suspeitas ou maliciosas.

### Quando você abriu um arquivo do tipo log, pôde observar qual é o formato padrão para armazenamento dos dados. Você pode transformar o formato de dados para JSON.

### Pare a execução do Zeek, digitando o comando:

    sudo /opt/zeek/bin/zeekctl stop

### Edite o arquivo a seguir e adicione o texto após a última linha:

    sudo nano /opt/zeek/share/zeek/site/local.zeek

    # Output to JSON
    @load policy/tuning/json-logs.zeek
    Salve pressionando "Ctrl + O", "Enter". Para sair do nano, pressione "Ctrl + X".

### Reinicie o Zeek.

    sudo su
    # /opt/zeek/bin/zeekctl start

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

### Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

    export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/FabriciaMM/g')"

Acesse novamente o arquivo conn.log.

    # cd /opt/zeek/logs/current
    # nano conn.log

### A partir de agora, os logs gravados em /opt/zeek/logs/current estarão no formato JSON. Obs.: Pode levar algum tempo para os registros aparecerem no arquivo. Faça a captura de tela desse arquivo.

### Para sair de uma visualização, pressione "q" quando visualizar (END) no rodapé.

### Veja um exemplo de arquivo no formato JSON.

    {
      "ts": 1597593633.224633,
      "fuid": "FB4Sx62yaleypxnhIb",
      "tx_hosts": [
        "23.246.2.148"
      ],
      "rx_hosts": [
        "10.2.2.23"
      ],
      "conn_uids": [
        "CUgYfkjoZLP4BR8Ol"
      ],
      "source": "HTTP",
      "depth": 0,
      "analyzers": [
        "JPEG",
        "SHA1",
        "MD5",
        "SHA256"
      ],
      "mime_type": "image/jpeg",
      "duration": 0.01756000518798828,
      "local_orig": false,
      "is_orig": false,
      "seen_bytes": 58175,
      "total_bytes": 58175,
      "missing_bytes": 0,
      "overflow_bytes": 0,
      "timedout": false,
      "md5": "0671e92b0fb8ffe5724579c229a43689",
      "sha1": "e855561e88f0bc57733eafa05a9d7681d276e55a",
      "sha256": "fc58cf109988af3b3dbc499001ff300584eff638cb120405558d3df69c22fdf4"
    }

fuid (por exemplo, FB4Sx62yaleypxnhIb): Este é o ID exclusivo do arquivo. Tenha em mente que isso não é a mesma coisa que o "uid" que geralmente encontramos em outros registros do Zeek.

tx_hosts (por exemplo, 23.246.2.148): Este é o endereço do host que transferiu o arquivo.

rx_hosts (por exemplo, 10.2.2.23): Este é o endereço do host que recebeu o arquivo.

conn_uids (por exemplo, CUgYfkjoZLP4BR8Ol): Este ID exclusivo é equivalente ao "uid" e é usado para correlacionar a atividade em conn.log e outros logs Zeek.

origem (por exemplo, HTTP): Este campo indica o protocolo usado para transferir o arquivo.

analisadores (por exemplo, JPEG, SHA1, MD5, SHA256): Estes são os analisadores de arquivo utilizados para analisar este arquivo.

mime_type (por exemplo, image/jpeg): Este campo é a suposição do Zeek sobre qual é o tipo MIME do arquivo.

vistos_bytes (por exemplo, 58175): Este é o número de bytes que o Zeek conseguiu observar.

total_bytes (por exemplo, 58175): Este é o número total de bytes que o arquivo deveria ter.

missing_bytes (por exemplo, 0): Este é o número de bytes que estavam faltando na análise, provavelmente devido à perda de pacotes.

overflow_bytes (por exemplo, 0): Este é o número de bytes que não foram analisados devido a bytes sobrepostos ou erros de remontagem.

md5 (por exemplo, 0671e92b0fb8ffe5724579c229a43689): Este é o hash MD5 do arquivo.

sha1 (por exemplo, e855561e88f0bc57733eafa05a9d7681d276e55a): Este é o hash SHA1 do arquivo.

sha256 (por exemplo, fc58cf109988af3b3dbc499001ff300584eff638cb120405558d3df69c22fdf4): Este é o hash SHA256 do arquivo.

