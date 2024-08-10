# Atividade 3.4 - Extração automática de arquivos
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Com o gerenciador de pacotes zkg instalado, vamos configurar as opções de extração de arquivo.

Neste exemplo, vamos definir o diretório para armazenar os arquivos extraídos e estabelecer que desejamos extrair automaticamente os tipos de arquivos frequentemente explorados (como Java, PE, Microsoft Office e PDF).

### Abra o arquivo /opt/zeek/share/zeek/site/file-extraction/config.zeek. Localize a linha que possui o texto module FileExtraction; e insira o texto a seguir, de modo que o bloco fique conforme mostrado.

    # exit
    $ sudo nano /opt/zeek/share/zeek/site/file-extraction/config.zeek

    module FileExtraction;
    #### Extracao automatica de arquivos
    # A linha a seguir configura onde os arquivos extraidos serao armazenados
    redef path = "/opt/zeek/extract_files/";
    # A linha a seguir configura 'plugins' que podem ser carregados
    # estes sao modulos de atalho para especificar 
    # politicas comuns de extracao de arquivos. Exemplo:
    # @load ./plugins/extract-pe.bro
    @load ./plugins/extract-common-exploit-types

### Agora, vamos criar o diretório que usaremos para salvar todos os arquivos extraídos. Esse diretório deve ser o mesmo que definimos em config.zeek. Você pode criar o diretório com o seguinte comando:

    sudo mkdir /opt/zeek/extract_files
### Se esta é a sua primeira vez instalando um pacote Zeek, edite o arquivo /opt/zeek/share/zeek/site/local.zeek e adicione as seguintes linhas no final do arquivo. Isso carregará todos os pacotes que você instalou. Você só precisa fazer isso uma vez:

    $ sudo nano /opt/zeek/share/zeek/site/local.zeek

    (...)

    # Carregar Pacotes Zeek
    @load packages
### O comando a seguir aplica as novas configurações e inicia o Zeek:

    $ sudo /opt/zeek/bin/zeekctl deploy
### Verifique e anote qual é a designação da interface de rede que será utilizada para escuta de conexão para a extração de arquivos.

    $ ip addr

<p>
<img width="500" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade3/atividade3a.PNG">
</p>
