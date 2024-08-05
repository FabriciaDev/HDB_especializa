# Atividade 1.5. Outras ferramentas
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Outra ferramenta muito útil disponível para usar junto com o Nmap é o comando curl. Com ele, você pode fazer uma varredura em qualquer endereço IP. Ele fornece ainda mais informações sobre esse IP, como localização, nome da organização, cidade e assim por diante. É um tipo de busca Whois, mas muito mais rica em detalhes. A única limitação é que você pode fazer varredura em apenas 1.000 IPs por dia. Se precisar de uma varredura massiva, vai precisar de uma máquina mais poderosa.

### Vamos supor que você queira saber a localização e outras informações sobre o <scanme.nmap.org>. Digite curl ipinfo.io/45.33.32.156 no seu terminal e você recebe o resultado imediatamente.

curl ipinfo.io/45.33.32.156

{

  "ip": "45.33.32.156",
  
  "hostname": "scanme.nmap.org",
  
  "city": "Fremont",
  
  "region": "California",
  
  "country": "US",
  
  "loc": "37.5483,-121.9886",
  
  "org": "AS63949 Akamai Connected Cloud",
  
  "postal": "94536",
  
  "timezone": "America/Los_Angeles",
  
  "readme": "https://ipinfo.io/missingauth"

} 

### De uma vez só, você tem tudo: cidade, região, CEP, país e nome da organização. Como você pode ver, o curl é uma ferramenta bem bacana.

Seja grande ou pequena, qualquer organização que esteja digitalmente conectada está sempre sob risco. Como um aspirante a especialista em testes de penetração, você precisa entender isso bem. Existem muitas ferramentas que podem te ajudar nesse trabalho, e uma as delas é o DMitry (Deepmagic Information Gathering Tool). Essa ferramenta coleta o máximo de informações possíveis.

### Usar o DMitry é simples. No terminal, você digita:

/bin/dmitry google.com

### Ele vai começar a te dar informações como essa:

//output from running DMitry HostIP:216.58.203.206

HostName:google.com

[...]

Você também pode obter informações sobre os subdomínios.

O DMitry é uma ferramenta bem útil. Ele reúne todas as informações que consegue sobre o host e faz uma varredura nas portas TCP do destino. Faz uma pesquisa Whois muito completa, recolhendo todos os dados possíveis de tempo de atividade, dados do sistema e do servidor.

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"

Se quiser, você ainda pode salvar todas as informações em um arquivo de texto. A partir do seu diretório de login (/home/aluno), é só digitar no terminal:

dmitry -wise -o dmitry.txt google.com

### Esse comando vai salvar tudo em um arquivo de texto chamado dmitry.txt no seu diretório de login. Realize a captura de tela do conteúdo do arquivo.

Referências
HackingLoops. How to Automate Web Reconnaissance Using Python Scripts. Disponível em: https://www.hackingloops.com/web-reconnaissance-using-python-scripts/. Acesso em: 12 jul 2023.

Sinha, Sanjib (2018) Beginning Ethical Hacking with Kali Linux. Apress Media LLC.

Tutorials Point. Python Penetration Testing - Quick Guide. Disponível em: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_quick_guide.htm. Acesso em: 12 jul 2023.

