# Gatinho Faminto 🐱🍕
Esse é meu primeiro jogo em Python! É um jogo bem simples onde você controla um gatinho que precisa coletar itens enquanto vai ficando maior a cada item pegado. Mas cuidado: se o gatinho bater nas bordas da tela, o jogo acaba! 😬

# Como jogar:
Use as setas do teclado (↑ ↓ ← →) para mover o gatinho.
Colete os itens (eles aparecem aleatoriamente na tela).
A cada 3 itens coletados, o gatinho cresce (fica mais forte!).
Se o gatinho colidir com as bordas da tela, o jogo acaba e você volta pro início. 😿

# Como rodar o jogo:
Se ainda não tem o Python instalado, baixe o Python.

# Clone o repositório:
git clone https://github.com/kartolina/gatinhogame.git

# Entre na pasta do projeto:
cd caminho/para/o/gatinhogame

# Instale as dependências:
pip install -r requirements.txt

# Execute o jogo:
python game3.py

# O que usei:
Python: A linguagem que usei para programar o jogo.
Pygame: Biblioteca para criação de jogos, com gráficos e sons.

# Melhorias que quero fazer:
Adicionar novos coletáveis e desafios.
Melhorar a animação do gatinho.
Deixar o jogo mais difícil com o tempo.
Adicionar sons e musica.

# Imagens:
toda a arte usada no jogo foi graças aos artistas no ichi.io que disponibilizaram seu trabalho para projetos como este: 9E0, edermunizz e Henry Software!





# Tutorial Detalhado
Como rodar o "Gatinho Faminto" no seu computador
Para rodar o jogo que você baixou, siga as instruções abaixo:

1. Baixando o projeto
Primeiro, baixe o projeto clicando no botão "Code" no GitHub e depois "Download ZIP".
Extraia o arquivo ZIP para uma pasta em seu computador.
2. Instalando o Python
Para rodar o jogo, você precisa ter o Python instalado. Aqui está como fazer isso:

Vá até o site do Python.
Baixe a versão mais recente do Python para o seu sistema operacional (Windows, macOS ou Linux).
Importante: Durante a instalação, marque a opção "Add Python to PATH", para garantir que você possa usar o Python diretamente no terminal.
3. Instalando as dependências
Agora que você tem o projeto e o Python instalados, precisamos instalar as bibliotecas necessárias para rodar o jogo.

Passo 1: Abrindo o terminal na pasta do projeto
Windows:

Navegue até a pasta onde você extraiu o projeto no File Explorer.
Clique na barra de endereços (onde está o caminho da pasta), apague o que está escrito lá e digite cmd, depois pressione Enter. Isso abrirá o Prompt de Comando dentro da pasta do projeto.
Mac/Linux:

Abra o Terminal e, com o comando cd, navegue até a pasta onde você extraiu o projeto. Exemplo:
bash
Copiar código
cd /caminho/para/a/pasta/do/projeto
Passo 2: Criando um ambiente virtual (opcional, mas recomendado)
Para evitar conflitos com outras versões de Python, é bom criar um ambiente virtual. Isso mantém tudo isolado.

No terminal, digite o seguinte comando para criar o ambiente virtual:
bash
Copiar código
python -m venv venv
Ative o ambiente virtual:
Windows:
bash
Copiar código
.\venv\Scripts\activate
Mac/Linux:
bash
Copiar código
source venv/bin/activate
Passo 3: Instalando as dependências
Com o ambiente virtual ativo, instale as dependências do projeto (que estão no arquivo requirements.txt).

No terminal, digite o seguinte comando:
bash
Copiar código
pip install -r requirements.txt
Isso vai baixar todas as bibliotecas que o jogo precisa para rodar.

4. Rodando o jogo
Agora que tudo está pronto, basta rodar o jogo!

No terminal, com o ambiente virtual ainda ativo, digite:
bash
Copiar código
python game3.py
