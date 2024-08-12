# Atividade 4.1 - Conhecendo o CyberChef
O CyberChef é projetado para criptografia, análise e manipulação de dados. A interface permite realizar uma variedade de operações como codificação e decodificação, realização de operações como XOR ou cálculos bit a bit, e manipulação de dados em formatos variados como JSON, XML e Base64. É muito usado por profissionais de segurança cibernética para análise de malware, decodificação de dados e resolução de puzzles complexos.

Desenvolvido pela Sede de Comunicações do Governo (GCHQ) no Reino Unido, o CyberChef é um aplicativo da web também chamado de “Cyber Swiss Army Knife” (em tradução livre, "Canivete cibernético suíço").

<p>
<img width="800" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade4/cyberchef1.PNG">
</p>

Acesse o CyberChef visitando o site:

https://gchq.github.io/CyberChef/.

Vamos começar por alguns casos de uso mais simples. No menu lateral à esquerda estão diferentes "ingredientes", que nada mais são do que as diversas operações oferecidas pelo CyberChef, e que podem adicionados para fazer uma "receita" (Recipe). No canto superior direito está a caixa de entrada ("Input") e abaixo dela está o texto de saída ("Output"). Deixe a caixa "Auto Bake" (algo como "auto cozimento") marcada.

## Análise de dados e decodificação
### Vamos inserir uma string codificada em Base64 para decodificá-la.

### Digite o texto codificado na caixa "Input", e clique duas vezes na operação "From Base64", localizado dentro do menu lateral "Data Format".

    ?VGhpcyBpcyBpIHN0cmluZw?

O resultado deverá ser:

This is i string

<p>
<img width="800" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade4/cyberchef2.PNG">
</p>

### Clique no ícone "Clear Recipe" (o ícone da lixeira), junto à caixa "Recipe".

## Encriptação e Descriptografia
Agora iremos descriptografar uma mensagem usando o algoritmo AES.

### Clique duas vezes na operação "From Base64", localizado dentro do menu lateral "Data Format", e insira o texto a seguir na caixa "Input":

    zZYksTFC3xS8415+Vg0Mu9Xa0TeTo+ndVi0jueSxsVjA1HXxewU+fKtkU2Gu53zA+RtlstITVO2JKkcIH1H48A==

### Depois, e clique duas vezes na operação "AES Decrypt", localizado dentro do menu lateral "Encryption/Encoding", e insira os dados a seguir nos campos que aparecem dentro da própria "Receita":

    Key (Chave): 55555555555555555555555555555555

    Tipo da Chave: UTF8

    IV (Vetor de Inicialização): 0000000000000000000000000000000

    Tipo do IV: HEX

    Mode: CBC

    Input: Raw

    Output: Raw

### O resultado deverá ser:

{"status":"ERROR_GENERIC","status_det":"INVALID_INPUT"}

<p>
<img width="800" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade4/cyberchef3.PNG">
</p>

### Clique no ícone "Clear Recipe" (o ícone da lixeira), junto à caixa "Recipe".

## Compressão e descompressão de dados

### Crie um arquivo txt com o nome "OlaMundo.txt", e dentro dele digite o texto: Olá Mundo!.

### Para comprimir o arquivo que você acabou de criar para o formato ZIP, utilize o seu compressor favorito no Windows (Winzip, WinRAR, 7-Zip, compactador nativo do sistema, etc.), ou no Linux (por exemplo, $ zip OlaMundo.zip OlaMundo.txt).

### Clique duas vezes na operação "Unzip", localizado dentro do menu lateral "Compression". Junto ao título da caixa "Input", mais à direita, localize o ícone "Open File As Input". Clique nele, navegue pelo seu computador para selecionar o arquivo Zip criado.

### Você deverá visualizar na caixa "Output" o arquivo "OlaMundo.zip" descompactado.

<p>
<img width="800" src="https://github.com/FabriciaDev/HDB_especializa/blob/main/Atividade4/cyberchef4.PNG">
</p>

## Manipulação de dados
>> REALIZAR A CAPTURA DE TELA DO RESULTADO OBTIDO NO PASSO A SEGUIR

O CyberChef fornece uma ampla gama de ferramentas de manipulação de dados, como XOR, operações bit a bit e manipulação de strings.

Vamos decodicar uma string que foi codificada com XOR.

### Clique duas vezes na operação "From Hex", localizado dentro do menu lateral "Data Format", e insira o texto a seguir na caixa "Input". Em "Delimiter", deixe marcada a opção "Auto".

    01160439247629711d242e76251d2472301d36713136732c253f

### Depois, clique duas vezes na operação "XOR Brute Force", localizado dentro do menu lateral "Arithmetic/Logic". Insira o "Input" a seguir:

    Key lenght: 1

    Sample lenght: 100

    Sample offset: 0

    Scheme: Standard

    Crib (known plaintext string): CTF{

O resultado no "Output" deverá ser:

Key = 42: CTF{f4k3_fl4g_f0r_t3st1ng}

### Realize a captura da tela que mostra o resultado obtido.
