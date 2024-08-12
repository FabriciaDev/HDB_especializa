Atividade Prática - Tratamento de Incidentes - Rede e Aplicativo Web
O Monitoramento de Segurança de Rede (NSM - Network Security Monitoring) é o processo de observar e analisar a sua rede em busca de eventos de segurança. Esse monitoramento pode ser feito de maneira proativa, como por exemplo ao identificar vulnerabilidades ou certificados SSL vencidos, ou de maneira reativa, como na resposta a incidentes e na análise forense de rede. Seja para acompanhar as atividades de um invasor ou para manter o malware sob controle, o NSM te dá contexto, inteligência e consciência da situação em sua rede.

O Monitoramento de Segurança Empresarial (ESM - Enterprise Security Monitoring) é um passo adiante do NSM, incluindo a visibilidade do endpoint e outros dados telemétricos de sua organização.

O conceito de NSM é diferente do conceito de IDS. Os fornecedores de detecção de intrusão estão focados no alerta e consideram seu trabalho concluído quando ativam a "luz vermelha piscando". O NSM assume que a prevenção eventualmente falha e alguns invasores são mais espertos do que você: "Prepare-se para o pior coletando tudo o que puder, técnica e legalmente".

Considere a situação em que queremos utilizar o processo NSM em uma rede corporativa típica, com firewall, estações de trabalho e servidores. Você pode usar um conjunto de ferramentas para monitorar o tráfego com o objetivo de detectar um invasor infiltrando-se no ambiente, estabelecendo comando e controle (C2) ou talvez realizando exfiltração de dados. Provavelmente, também será do seu interesse monitorar o tráfego para identificar movimentos laterais. Com o aumento do tráfego criptografado em nossas redes, é crucial suplementar essas áreas cegas com visibilidade adicional através da telemetria de endpoint. Podemos processar logs dos servidores e estações de trabalho, permitindo que você faça pesquisas abrangentes em toda a sua rede e registre logs simultaneamente.

Um exemplo de plataforma NSM e de código aberto é o Security Onion, que integra várias ferramentas como por exemplo o Kibana (ferramenta de visualização e exploração de dados), o Grafana (plataforma de análise e monitoramento open-source, excelente para visualizar dados de séries temporais, com suporte a várias fontes de dados), o CyberChef (projetado para criptografia, análise e manipulação de dados), o FleetDM (ferramenta de gerenciamento centralizado open-source focada no osquery).

Além disso, uma ferramenta NSM pode possibilitar, por exemplo, criar e editar playbooks; utilizar uma instância local do MITRE ATT&CK Navigator; emitir alertas vindos de sistemas de detecção de intrusão como Suricata e Snort; personalizar painéis que permitem aos analistas monitorar e visualizar dados de rede e eventos de segurança; buscar proativamente por sinais de comprometimento ou atividades suspeitas nos dados de rede; criar e gerenciar casos para documentar e rastrear suas investigações; capturar pacotes (PCAP); dentre outros recursos.

Vamos a seguir explorar algumas ferramentas que podem compor um processo NSM.

Instruções para entrega da Atividade Prática
Leia com atenção!
No final deste módulo você deve submeter em um ÚNICO arquivo PDF as seguintes capturas de tela:

Atividade 4.1: passo 4.

Atividade 4.2: passo 5.

Atividade 4.4: passo 2.

Atividade 4.5: passo 9.

No mesmo arquivo PDF onde se encontram as capturas de tela, inclua o desenvolvimento do exercício da(s) atividade(s) a seguir, usando para isso um editor de textos, como p. ex. Microsoft Word ou Apache OpenOffice Writer:

Atividade 4.3: passo 1.

O arquivo deverá conter:

O seu nome completo;

Para atividades textuais:

As transcrições dos enunciados de cada uma das atividades e das perguntas, com o desenvolvimento das suas respectivas respostas.

Para atividades de uso de sistemas computacionais:

O título de cada atividade, que irá conter a resposta de cada passo identificada pelo seu respectivo número;

Caso a resposta seja uma captura de tela do prompt, substitua o nome de usuário no terminal para o seu nome e sobrenome, configurados como um alias (apelido), juntamente com a data e hora atuais. Por exemplo, se o se nome é "Meu Nome", no início da tarefa, execute o comando:

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Obs.: Você terá que digitar o comando acima cada vez que acessar o terminal do Linux.

A captura de tela do prompt deverá mostrar o comando digitado e a saída (output) deste comando. Caso seja necessário, enviar uma captura de tela contendo o comando, e outra captura de tela contendo a saída em tela, por exemplo, quando o texto da saída suprimir o texto do comando digitado.
