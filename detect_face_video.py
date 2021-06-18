import cv2

# carregue o cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Para capturar vídeo da webcam.
cap = cv2.VideoCapture(0)
# Para usar um arquivo de vídeo como entrada
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Leia o frame
    _, img = cap.read()

    # Converte para grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta o rosto
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Desenhe o retângulo ao redor de cada rosto
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exibir
    cv2.imshow('img', img)

    # Pare se a tecla Escape for pressionada
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Libere o objeto VideoCapture
cap.release()