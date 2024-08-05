# Atividade 1.4 - Um pouco sobre varredura

Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Ser capaz de fazer uma varredura sem ser detectado é um desafio perfeito para um hacker. No entanto, como especialista em segurança cibernética, sua prioridade deve ser proteger seu próprio sistema. A ética do hacking não é apenas sobre ataque, mas também sobre autodefesa.

Vamos falar um pouco sobre footprinting, algo como "pegadas digitais". Imagine a seguinte situação: você se depara com um endereço IP vindo do Panamá. Se você resolver pesquisar esse endereço IP em um serviço Whois, você pode ficar bem surpreso. Sabe por quê? Muitos dos endereços IP por aí não seguem as melhores práticas de segurança. Não é raro encontrar informações valiosas como endereços completos, contatos, IDs de administradores e muito mais coisas que, na real, não deveriam ser disponibilizadas assim tão facilmente.

A pesquisa Whois pode ser usada para qualquer URL. E tem mais: você pode fazer a ação contrária usando o terminal da sua máquina virtual Linux. Existe um comando bem útil chamado nslookup. É só digitá-lo na linha de comando junto com qualquer extensão de URL, e você recebe o endereço IP correspondente.

### Vamos ver como isso funciona. Veja o seguinte comando:

nslookup scanme.nmap.org

Server:         10.0.2.3

Address:        10.0.2.3#53


Non-authoritative answer:

Name:   scanme.nmap.org

Address: 45.33.32.156

Name:   scanme.nmap.org

Address: 2600:3c01::f03c:91ff:fe18:bb2f

O número na segunda linha (#53) indica a porta para um servidor DNS. O anonimato é super importante no mundo do hacking ético. Você pode usar navegadores como o Tor ou alterar as configurações do sistema para manter o anonimato enquanto usa ferramentas de hacking.

### E se você tiver um endereço IP? A pesquisa reversa também é bem fácil com o comando nslookup. Vamos tentar isso com o endereço IP de scanme.nmap.org no Linux:

nslookup 45.33.32.156

156.32.33.45.in-addr.arpa       name = scanme.nmap.org.


Authoritative answers can be found from:

32.33.45.in-addr.arpa   nameserver = ns5.linode.com.

32.33.45.in-addr.arpa   nameserver = ns3.linode.com.

32.33.45.in-addr.arpa   nameserver = ns1.linode.com.

32.33.45.in-addr.arpa   nameserver = ns2.linode.com.

32.33.45.in-addr.arpa   nameserver = ns4.linode.com.

### A diferença mais uma vez fica por conta do endereço do servidor. Mas tem outra coisa legal aqui:

156.32.33.45.in-addr.arpa	name = scanme.nmap.org.

O endereço IP de scanme.nmap.org é mostrado na ordem inversa. Bacana, né?

A gente ainda não acabou com a varredura digital. Em alguns casos, quando você se aprofunda mais, pode ver que algumas varreduras podem levar dias para terminar. Por agora, vamos continuar olhando para o scanme.nmap.org e tentar descobrir quantas portas estão abertas lá.

### >> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

export PS1="$(echo "\d \t $PS1"|sed -e 's/\u/FabriciaMM/g')"

### Volte ao Nmap e digite o comando:

Copy
 nmap scanme.nmap.org -vv

### O resultado vai mostrar algumas informações interessantes. Realize a captura de tela do resultado.

Repare na última parte do resultado. Tem uma lista que mostra quantas portas estão abertas. Isso já dá uma ideia do que é uma varredura real.

