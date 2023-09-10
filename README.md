# Detectar Rosto com OpenCV

Este é um projeto simples para detectar rostos em imagens e vídeo usando a biblioteca OpenCV em Python. Ele inclui dois scripts: um para detectar rostos em uma imagem estática e outro para detectar rostos em um vídeo, como a partir de uma webcam.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema e também instale a biblioteca OpenCV se ainda não a tiver. Você também precisará do arquivo `haarcascade_frontalface_default.xml`, que é um classificador pré-treinado para detecção de faces.

## Como Usar

### Detecção de Rosto em Imagem (detect_face.py)

1. Baixe ou crie uma imagem que contenha rostos a serem detectados.

2. Execute o script `detect_face.py` e ajuste o caminho da imagem no código para a imagem que deseja processar.

3. O script detectará automaticamente os rostos na imagem e desenhará retângulos ao redor deles.

4. A imagem resultante com os retângulos será exibida.

### Detecção de Rosto em Vídeo (detect_face_video.py)

1. Certifique-se de que sua webcam esteja funcionando corretamente.

2. Execute o script `detect_face_video.py`. Ele usará a webcam padrão como fonte de vídeo, mas você também pode usar um arquivo de vídeo fornecendo o caminho correto.

3. O script detectará rostos no vídeo em tempo real e desenhará retângulos ao redor deles.

4. A janela de vídeo ao vivo exibirá os rostos detectados em tempo real.

5. Pressione a tecla "Esc" (Escape) para encerrar o programa.

## Notas

- O script usa o classificador `haarcascade_frontalface_default.xml` pré-treinado para detectar rostos. Você pode encontrar esse arquivo em recursos do OpenCV ou baixá-lo diretamente do repositório do OpenCV.

- Você pode personalizar os parâmetros da função `detectMultiScale` para ajustar a sensibilidade da detecção de rostos.

- Este é um projeto simples de detecção de rosto e não inclui funcionalidades avançadas, como identificação de rosto ou rastreamento de rosto em vídeo em tempo real.

Divirta-se explorando a detecção de rostos com OpenCV!
