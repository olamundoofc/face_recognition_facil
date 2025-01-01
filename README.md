# Sistema de Reconhecimento Facial em Python
Este repositório contém um projeto simples para criação de um sistema de reconhecimento facial em Python, utilizando as bibliotecas face_recognition e opencv-python. Com menos de 30 linhas de código, é possível detectar e reconhecer um rosto em tempo real através da webcam.

## Como funciona?
O sistema utiliza a câmera do seu computador para capturar frames e, a cada frame, realiza a detecção de rostos presentes na imagem. Quando encontra um rosto que corresponde à imagem de referência carregada previamente, exibe uma mensagem indicando que o rosto foi reconhecido.

## Pré-requisitos
Antes de executar o código, é necessário instalar as bibliotecas que utilizamos. No terminal ou prompt de comando, execute:
```
pip install face_recognition opencv-python
```
## Como usar
Baixe ou clone o repositório:
```
git clone https://github.com/olamundoofc/reconhecimento_facial_30_linhas
cd reconhecimento_facial_30_linhas
```
Prepare a imagem de referência:

Coloque uma imagem do seu rosto ou de outra pessoa que deseja reconhecer dentro da pasta do projeto.
Renomeie a imagem para meu_rosto.jpg ou altere o código para usar o nome correto da sua imagem.

No terminal, execute:
```
python app.py
```
Isso abrirá a janela da webcam. O sistema começará a capturar imagens e procurar um rosto correspondente à imagem de referência. Quando o rosto for reconhecido, será exibida a mensagem "Rosto reconhecido!" no vídeo.
