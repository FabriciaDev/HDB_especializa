# Atividade 1.3 - Reconhecimento
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

O reconhecimento é uma etapa essencial na fase inicial do teste de penetração, onde se coleta o máximo possível de informações sobre o alvo. Esta fase inclui a coleta de informações de domínio público, bem como o uso de ferramentas mais sofisticadas para obter mais detalhes sobre o alvo.

Você pode usar desde o Traceroute, até outras ferramentas como recon-ng, DMitry, Maltego. Como estamos trabalhando com Python, vamos dar uma olhada na ferramenta FinalRecon.

O FinalRecon é uma ferramenta de inteligência de código aberto utilizada em projetos de reconhecimento baseados na web. Ela tem o superpoder de detectar e coletar informações úteis sobre domínios alvo de forma automática. A estrutura modular da ferramenta permite expandir seus recursos de reconhecimento. Vamos dar uma olhada nas características dessa poderosa ferramenta.

* Informação WHOIS: Essencial para saber quem está por trás de um determinado domínio.

* Informações do Cabeçalho: Dá uma visão das respostas HTTP que o servidor fornece.

* Registro de Certificado SSL: Mostra detalhes sobre o certificado de segurança do site.

* Enumeração DNS: Revela informações sobre os registros DNS do domínio.

* Listagem de Subdomínios: Mapeia todos os subdomínios ligados ao domínio principal.

* Informações de Rastreamento de Rota: Fornece a rota que os pacotes seguem até o servidor.

* Busca no Diretório: Permite encontrar diretórios ocultos ou esquecidos.

* Varredura de Portas: Identifica portas abertas que possam ser exploradas.

* Rastreamento Web: Analisa o site para identificar conteúdo e links.

Cada um desses recursos de reconhecimento gera um monte de informações valiosas. Para os testadores de penetração, ajuda na identificação de pontos de injeção potenciais nos hosts alvo.

### Uma vez instalada, você pode ver como usar a ferramenta digitando:

python3 /opt/FinalRecon/finalrecon.py -h

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

export PS1="$(echo "\d \t $PS1"|sed -e 's/\u/FabriciaMM/g')"

### Verifique o certificado SSL. Substitua o endereço https://www.dominio.com por um site bem conhecido, por exemplo, Google ou Cloudflare.  Faça a captura de tela do comando digitado contendo a respectiva saída na tela.

python3 /opt/FinalRecon/finalrecon.py --sslinfo https://www.google.com

### Agora experimente digitar os comandos a seguir um de cada vez, e veja quais são as saídas no terminal. Substitua o endereço https://www.dominio.com por um site bem conhecido, por exemplo, Google ou Cloudflare.

Verificar cabeçalhos:

python3 /opt/FinalRecon/finalrecon.py --headers https://www.google.com
Verificar as informações do whois:

python3 /opt/FinalRecon/finalrecon.py --whois  https://www.google.com
Alvo de rastreamento:

python3 /opt/FinalRecon/finalrecon.py --crawl https://www.google.com
Verificação completa:

python3 /opt/FinalRecon/finalrecon.py --full https://www.google.com
