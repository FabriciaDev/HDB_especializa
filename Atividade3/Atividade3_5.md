# Atividade 3.5 - Caso de uso do dia a dia
Você irá executar essa atividade na VM forenseLinux. Após logar e acessar a máquina landing, abra o RDP (Conexão de Área de Trabalho Remota), e digite o endereço IP: 192.168.98.10.

Suponha que um usuário recebeu um e-mail com um link malicioso, supostamente relacionado ao pagamento do bônus trimestral dos funcionários. O usuário clica no link e imediatamente faz o download de um arquivo. Queremos saber se o arquivo é malicioso e, se for, identificar as medidas que podemos tomar para impedir que outros sistemas façam o download do mesmo arquivo.

Configuramos anteriormente a nossa instância do Zeek para fazer automaticamente o hash de todos os arquivos, extrair arquivos do Windows PE e realizar consultas no Registro de Hash de Malware da Team Cymru.

Primeiramente, somos notificados de atividades suspeitas por meio de um alerta gerado no notice.log.

Obs.: O Zeek oferece dois logs para atividades que parecem fora do comum:

weird.log: Coisas aleatórias em que os analisadores tiveram problemas para entender o tráfego em termos de seus protocolos. Sempre que há algo inesperado no nível do protocolo, isso é "estranho" (por falta de algo melhor para fazer com isso).

notice.log: Avisos de situações explicitamente detectadas e relatadas pelos scripts Zeek como dignas de inspeção. Geralmente não são erros de protocolo, mas algo semanticamente superior (como um certificado autoassinado).

Situações estranhas muitas vezes podem ser ignoradas por causa do volume, mas os avisos são muito mais interessantes, eles são o que Zeek mais se aproxima dos alertas de IDS.

A entrada de log abaixo traz as seguintes informações:

O tipo MIME do arquivo é application/x-dosexec.

O aviso se trata de um "Match" do Registro de Hash de Malware da TeamCymru.

Há uma taxa de detecção da Team Cymru de 38%.

O aviso fornece um link direto para o arquivo suspeito no VirusTotal, nos quais quase todos os scanners identificam esse arquivo como malicioso.

Pelos nomes de detecção, isso está relacionado ao ransomware WannaCry.

O arquivo veio do IP 149.202.220.122, baixado pelo host 10.2.2.23.

Copy
{
  "ts": 1597850503.829048,
  "uid": "CO3tTx2lknzNvQe7P3",
  "id.orig_h": "10.2.2.23",
  "id.orig_p": 56197,
  "id.resp_h": "149.202.220.122",
  "id.resp_p": 80,
  "fuid": "F1sCdV2rXJ9afKdlP2",
  "file_mime_type": "application/x-dosexec",
  "file_desc": "http://s000.tinyupload.com/_download_.php?file_id=91645583928538055155&t=9164558392853805515507216",
  "proto": "tcp",
  "note": "TeamCymruMalwareHashRegistry::Match",
  "msg": "_Malware_ Hash Registry Detection rate: 38%  Last seen: 2020-06-05 08:29:39",
  "sub": "https://www.virustotal.com/en/search/?query=5ff465afaabcbf0150d1a3ab2c2e74f3a4426467",
  "src": "10.2.2.23",
  "dst": "149.202.220.122",
  "p": 80,
  "peer_descr": "worker-1-2",
  "actions": [
    "Notice::ACTION_LOG"
  ],
  "suppress_for": 3600
}
Utilizando o UID CO3tTx2lknzNvQe7P3 do aviso, faremos uma pesquisa nos nossos logs por atividades relacionadas e veremos o que surge. Podemos procurar isso no Splunk ou usar o comando grep. Suponha que usamos o grep, e encontramos atividades relacionadas em:

conn.log: Vemos que o arquivo foi transferido via HTTP.

Copy
{
  "ts": 1597850493.368458,
  "uid": "CO3tTx2lknzNvQe7P3",
  "id.orig_h": "10.2.2.23",
  "id.orig_p": 56197,
  "id.resp_h": "149.202.220.122",
  "id.resp_p": 80,
  "proto": "tcp",
  "service": "http",
  "duration": 113.54712104797363,
  "orig_bytes": 624,
  "resp_bytes": 3514699,
  "conn_state": "RSTR",
  "local_orig": true,
  "local_resp": false,
  "missed_bytes": 0,
  "history": "ShADadfr",
  "orig_pkts": 1398,
  "orig_ip_bytes": 73512,
  "resp_pkts": 2433,
  "resp_ip_bytes": 3641211
}
http.log: O usuário 10.2.2.23 fez uma solicitação GET para "s000.tinyupload.com" para baixar um arquivo. Temos informações do ID exclusivo do arquivo (F1sCdV2rXJ9afKdlP2), so nome do arquivo (bonus.exe) e o tipo MIME do arquivo (aplicativo/x-dosexec).

Copy
{
  "ts": 1597850493.556732,
  "uid": "CO3tTx2lknzNvQe7P3",
  "id.orig_h": "10.2.2.23",
  "id.orig_p": 56197,
  "id.resp_h": "149.202.220.122",
  "id.resp_p": 80,
  "trans_depth": 1,
  "method": "GET",
  "_host_": "s000.tinyupload.com",
  "uri": "/_download_.php?file_id=91645583928538055155&t=9164558392853805515507216",
  "referrer": "http://s000.tinyupload.com/index.php?file_id=91645583928538055155",
  "version": "1.1",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
  "request_body_len": 0,
  "response_body_len": 3514368,
  "status_code": 200,
  "status_msg": "OK",
  "tags": [],
  "resp_fuids": [
    "F1sCdV2rXJ9afKdlP2"
  ],
  "resp_filenames": [
    "bonus.exe"
  ],
  "resp_mime_types": [
    "application/x-dosexec"
  ]
}
files.log: Além das informações que já constam no http.log, temos também os hashes MD5, SHA1 e SHA256 do arquivo. Como ativamos a extração automática de arquivos, o campo "extracted" nos informa para onde Zeek extraiu uma cópia do arquivo (/opt/zeek/extracted/HTTP-F1sCdV2rXJ9afKdlP2.exe). O Zeek foi capaz de analisar com sucesso e extrair o arquivo em sua totalidade, pois o campo "seen_bytes" corresponde a "total_bytes", e "missing_bytes" tem valor 0.

Copy
{
  "ts": 1597850493.672357,
  "fuid": "F1sCdV2rXJ9afKdlP2",
  "tx_hosts": [
    "149.202.220.122"
  ],
  "rx_hosts": [
    "10.2.2.23"
  ],
  "conn_uids": [
    "CO3tTx2lknzNvQe7P3"
  ],
  "source": "HTTP",
  "depth": 0,
  "analyzers": [
    "SHA1",
    "EXTRACT",
    "PE",
    "MD5",
    "SHA256"
  ],
  "mime_type": "application/x-dosexec",
  "filename": "bonus.exe",
  "duration": 10.055749893188477,
  "local_orig": false,
  "is_orig": false,
  "seen_bytes": 3514368,
  "total_bytes": 3514368,
  "missing_bytes": 0,
  "overflow_bytes": 0,
  "timedout": false,
  "md5": "84c82835a5d21bbcf75a61706d8ab549",
  "sha1": "5ff465afaabcbf0150d1a3ab2c2e74f3a4426467",
  "sha256": "ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa",
  "extracted": "/opt/zeek/extracted/HTTP-F1sCdV2rXJ9afKdlP2.exe",
  "extracted_cutoff": false
}
A partir daqui, podemos usar nossos sistemas de segurança de endpoint, bloquear os hashes de arquivos identificados ou o IP/URL nas nossas plataformas de segurança de rede e endpoint, realizar análises mais profundas e gerar Indicadores de Comprometimento (IOCs) e inteligência de ameaças adicionais, dentre outras ações.

Caso enfrente problemas com a captura de arquivos no Zeek:

Verifique se a captura completa de pacotes está sendo realizada: Podemos configurar o sistema para a captura completa de pacotes. Não abordaremos isso aqui.

Verifique se há perda de pacotes: Se o seu sensor Zeek ou TAP (Test Access Point) de rede estiver sobrecarregado, é possível que os pacotes estejam sendo descartados. Isso pode fazer com que alguns arquivos não apareçam em files.log ou que a extração automática falhe. Para verificar as estatísticas de rede para todas as interfaces de rede que o Zeek está monitorando:

Copy
$ sudo /opt/zeek/bin/zeekctl netstats
A coluna "dropped" indica o número de pacotes que foram descartados. Se este número for significativo, pode ser necessário otimizar o desempenho do Zeek ou adicionar mais capacidade à sua infraestrutura de monitoramento de rede.

Além disso, sempre certifique-se de que o hardware do sensor Zeek seja adequado para o volume de tráfego que você espera monitorar. Por fim, sempre é uma boa ideia revisar os logs regularmente para identificar quaisquer problemas potenciais. Por exemplo, o log reporter.log contém mensagens sobre problemas que o Zeek encontrou ao analisar o tráfego de rede, o que pode ajudar a identificar problemas com a captura de arquivos.

>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

Se ainda não o fez, configure o prompt no formato requerido para a entrega da atividade (troque "meunome" pelo seu próprio nome e sobrenome):

Copy
$ export PS1="$(echo "\d \t $PS1"|sed -e 's/\\u/meunome/g')"
Abra o arquivo conn.log, localize o uid em qualquer uma das linhas, e com ou mouse faça uma seleção do texto ("highlight") destacando o seu respectivo valor.

Copy
$ sudo su
# cd /opt/zeek/logs/current
# nano conn.log
Depois que terminar, saia do modo superusuário.

Copy
# exit
Referências
CHAN Fook Sheng | Medium. File extraction with Zeek. Disponível em: https://chanfs.medium.com/file-extraction-with-zeek-2c1a0bb1aa98. Acesso em: 21 jul 2023.

ericooi.com. Zeekurity Zen - Part II: Zeek Package Manager. Disponível em: https://ooiventures.com/zeekurity-zen-part-ii-zeek-package-manager/?_gl=11urfozh_gaMTU2NzM0NDIzNy4xNzE5MTEyNDc3_ga_CWB6FSZ962*MTcxOTE2NDcwMC4yLjEuMTcxOTE2NDc0MC4wLjAuMA... Acesso em: 23 jun 2024.

ericooi.com. Zeekurity Zen – Part VI: Zeek File Analysis Framework. Disponível em: https://ooiventures.com/zeekurity-zen-part-vi-zeek-file-analysis-framework/?_gl=116c2ph7_gaMTU2NzM0NDIzNy4xNzE5MTEyNDc3_ga_CWB6FSZ962*MTcxOTE2NDcwMC4yLjEuMTcxOTE2NDc5NS4wLjAuMA... Acesso em: 23 jun 2024.

How to Install Zeek Network Security Monitoring Tool on Ubuntu 22.04. Disponível em: https://www.howtoforge.com/how-to-install-zeek-network-security-monitoring-tool-on-ubuntu-22-04/. Acesso em: 19 jul 2023.

Jason Murray. Zeek Installation and Splunk CIM Data Normalization Guide. Disponível em: https://jasonmurray.org/posts/2022/zeekinstallandsplunklog/. Acesso em: 21 jul 2023.

Zeek Documentation — Book of Zeek (git/master). Disponível em: https://docs.zeek.org/en/master/. Acesso em: 19 jul 2023.

Last updated 18 days ago
