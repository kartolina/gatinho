# Gatinho Faminto 🐱🍕
Esse é meu primeiro projeto em Python :) É um jogo bem simples onde você controla um gatinho que precisa se alimentar enquanto vai ficando maior a cada item. Se o gatinho bater nas bordas da tela, o jogo acaba... mas seu recorde fica gravado! 😬

# Como jogar:
Use as setas do teclado (↑ ↓ ← →) para mover o gatinho.
Colete os itens culinários (eles aparecem aleatoriamente na tela).
A cada 3 itens coletados, o gatinho cresce (fica de buchin cheio).
Se o gatinho colidir com as bordas da tela, o jogo acaba e você volta pro início. 😿

# Como rodar o jogo:
Se ainda não tem o Python instalado, baixe o Python.

# Clone o repositório:
 https://github.com/kartolina/gatinho.git

# Entre na pasta do projeto:
cd caminho/para/o/gatinhogame

# Instale as dependências:
pip install -r requirements.txt

# Execute o jogo:
python game3.py

# O que usei:
Python: A linguagem que usei para programar o jogo.
Pygame: Biblioteca para criação de jogos.

# Melhorias que quero fazer:
Adicionar novos coletáveis e desafios.
Melhorar a animação do gatinho.
Deixar o jogo mais difícil com o tempo.
Adicionar sons e musica.

# Imagens:
toda a arte usada no jogo foi graças aos artistas no ichi.io que disponibilizaram seu trabalho para projetos como este: 9E0, edermunizz e Henry Software!


<3<3<3<3<3<3


# Tutorial Detalhado
# Gatinho Faminto

## Como rodar o jogo no seu computador

Siga as instruções abaixo para rodar o "Gatinho Faminto" e começar a jogar.

### 1. Baixando o projeto

1. **Baixe o projeto** clicando no botão **"Code"** no GitHub e depois **"Download ZIP"**.
2. Extraia o arquivo ZIP para uma pasta no seu computador.

### 2. Instalando o Python

Para rodar o jogo, você precisa ter o **Python** instalado no seu computador. 

1. Vá até o [site oficial do Python](https://www.python.org/downloads/).
2. Baixe a versão mais recente do Python para o seu sistema operacional (Windows, macOS ou Linux).
3. **Importante**: Durante a instalação, **marque a opção** "Add Python to PATH", para garantir que você possa usar o Python diretamente no terminal.

### 3. Instalando as dependências

Agora que você tem o projeto e o Python instalados, é hora de instalar as dependências necessárias para rodar o jogo.

#### Passo 1: Abrindo o terminal na pasta do projeto

- **Windows**: 
  1. Navegue até a pasta onde você extraiu o projeto no **File Explorer**.
  2. Clique na barra de endereços (onde está o caminho da pasta), apague o que está escrito lá e digite `cmd`, depois pressione Enter. Isso abrirá o **Prompt de Comando** dentro da pasta do projeto.

- **Mac/Linux**:
  1. Abra o **Terminal** e, com o comando `cd`, navegue até a pasta onde você extraiu o projeto:
     ```
     cd /caminho/para/a/pasta/do/projeto
     ```

#### Passo 2: Criando um ambiente virtual (opcional, mas recomendado)

Criar um ambiente virtual ajuda a manter as dependências do projeto isoladas.

1. No terminal, digite o seguinte comando para criar o ambiente virtual:
   ```
   python -m venv venv
Ative o ambiente virtual:
Windows:
```
.\venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```
Passo 3: Com o ambiente virtual ativo, instale as dependências do projeto (que estão no arquivo requirements.txt).

No terminal, digite o seguinte comando:
```
pip install -r requirements.txt
```
4. Rodando o jogo
Agora que tudo está configurado, basta rodar o jogo!

No terminal, com o ambiente virtual ainda ativo, digite:
```
python game3.py
```

