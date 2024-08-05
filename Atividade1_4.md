Atividade 1.4 - Um pouco sobre varredura
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Ser capaz de fazer uma varredura sem ser detectado é um desafio perfeito para um hacker. No entanto, como especialista em segurança cibernética, sua prioridade deve ser proteger seu próprio sistema. A ética do hacking não é apenas sobre ataque, mas também sobre autodefesa.

Vamos falar um pouco sobre footprinting, algo como "pegadas digitais". Imagine a seguinte situação: você se depara com um endereço IP vindo do Panamá. Se você resolver pesquisar esse endereço IP em um serviço Whois, você pode ficar bem surpreso. Sabe por quê? Muitos dos endereços IP por aí não seguem as melhores práticas de segurança. Não é raro encontrar informações valiosas como endereços completos, contatos, IDs de administradores e muito mais coisas que, na real, não deveriam ser disponibilizadas assim tão facilmente.

A pesquisa Whois pode ser usada para qualquer URL. E tem mais: você pode fazer a ação contrária usando o terminal da sua máquina virtual Linux. Existe um comando bem útil chamado nslookup. É só digitá-lo na linha de comando junto com qualquer extensão de URL, e você recebe o endereço IP correspondente.

Vamos ver como isso funciona. Veja o seguinte comando:

Copy
$ nslookup scanme.nmap.org
Server:         10.0.2.3
Address:        10.0.2.3#53

Non-authoritative answer:
Name:   scanme.nmap.org
Address: 45.33.32.156
Name:   scanme.nmap.org
Address: 2600:3c01::f03c:91ff:fe18:bb2f
O número na segunda linha (#53) indica a porta para um servidor DNS. O anonimato é super importante no mundo do hacking ético. Você pode usar navegadores como o Tor ou alterar as configurações do sistema para manter o anonimato enquanto usa ferramentas de hacking.

E se você tiver um endereço IP? A pesquisa reversa também é bem fácil com o comando nslookup. Vamos tentar isso com o endereço IP de scanme.nmap.org no Linux:

Copy
$ nslookup 45.33.32.156
156.32.33.45.in-addr.arpa       name = scanme.nmap.org.

Authoritative answers can be found from:
32.33.45.in-addr.arpa   nameserver = ns5.linode.com.
32.33.45.in-addr.arpa   nameserver = ns3.linode.com.
32.33.45.in-addr.arpa   nameserver = ns1.linode.com.
32.33.45.in-addr.arpa   nameserver = ns2.linode.com.
32.33.45.in-addr.arpa   nameserver = ns4.linode.com.
A diferença mais uma vez fica por conta do endereço do servidor. Mas tem outra coisa legal aqui:

Copy
156.32.33.45.in-addr.arpa	name = scanme.nmap.org.
O endereço IP de scanme.nmap.org é mostrado na ordem inversa. Bacana, né?

A gente ainda não acabou com a varredura digital. Em alguns casos, quando você se aprofunda mais, pode ver que algumas varreduras podem levar dias para terminar. Por agora, vamos continuar olhando para o scanme.nmap.org e tentar descobrir quantas portas estão abertas lá.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Volte ao Nmap e digite o comando:

Copy
$ nmap scanme.nmap.org -vv
O resultado vai mostrar algumas informações interessantes. Realize a captura de tela do resultado.

Repare na última parte do resultado. Tem uma lista que mostra quantas portas estão abertas. Isso já dá uma ideia do que é uma varredura real.

Atividade 1.5. Outras ferramentas
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Outra ferramenta muito útil disponível para usar junto com o Nmap é o comando curl. Com ele, você pode fazer uma varredura em qualquer endereço IP. Ele fornece ainda mais informações sobre esse IP, como localização, nome da organização, cidade e assim por diante. É um tipo de busca Whois, mas muito mais rica em detalhes. A única limitação é que você pode fazer varredura em apenas 1.000 IPs por dia. Se precisar de uma varredura massiva, vai precisar de uma máquina mais poderosa.

Vamos supor que você queira saber a localização e outras informações sobre o <scanme.nmap.org>. Digite curl ipinfo.io/45.33.32.156 no seu terminal e você recebe o resultado imediatamente.

Copy
$ curl ipinfo.io/45.33.32.156
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
De uma vez só, você tem tudo: cidade, região, CEP, país e nome da organização. Como você pode ver, o curl é uma ferramenta bem bacana.

Seja grande ou pequena, qualquer organização que esteja digitalmente conectada está sempre sob risco. Como um aspirante a especialista em testes de penetração, você precisa entender isso bem. Existem muitas ferramentas que podem te ajudar nesse trabalho, e uma as delas é o DMitry (Deepmagic Information Gathering Tool). Essa ferramenta coleta o máximo de informações possíveis.

Usar o DMitry é simples. No terminal, você digita:

Copy
$ /bin/dmitry google.com
Ele vai começar a te dar informações como essa:

Copy
//output from running DMitry HostIP:216.58.203.206
HostName:google.com

[...]
Você também pode obter informações sobre os subdomínios.

O DMitry é uma ferramenta bem útil. Ele reúne todas as informações que consegue sobre o host e faz uma varredura nas portas TCP do destino. Faz uma pesquisa Whois muito completa, recolhendo todos os dados possíveis de tempo de atividade, dados do sistema e do servidor.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Se quiser, você ainda pode salvar todas as informações em um arquivo de texto. A partir do seu diretório de login (/home/aluno), é só digitar no terminal:

Copy
$ dmitry -wise -o dmitry.txt google.com
Esse comando vai salvar tudo em um arquivo de texto chamado dmitry.txt no seu diretório de login. Realize a captura de tela do conteúdo do arquivo.

Referências
HackingLoops. How to Automate Web Reconnaissance Using Python Scripts. Disponível em: https://www.hackingloops.com/web-reconnaissance-using-python-scripts/. Acesso em: 12 jul 2023.

Sinha, Sanjib (2018) Beginning Ethical Hacking with Kali Linux. Apress Media LLC.

Tutorials Point. Python Penetration Testing - Quick Guide. Disponível em: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_quick_guide.htm. Acesso em: 12 jul 2023.

Last updated 14 days ago
