import cv2

# carregue o cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Leia a imagem de entrada
img = cv2.imread('adri.png')

# Converter em grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar rostos
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Desenhe o retângulo ao redor de cada rosto
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibir a saida
cv2.imshow('img', img)
cv2.waitKey()