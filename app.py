import face_recognition  
import cv2  

# Inicializa a webcam  
video_capture = cv2.VideoCapture(0)  

# Carrega uma imagem do rosto que queremos reconhecer  
known_image = face_recognition.load_image_file("meu_rosto.jpg")  
known_encoding = face_recognition.face_encodings(known_image)[0]  

# Loop para capturar frames da webcam  
while True:  
    ret, frame = video_capture.read()  
    rgb_frame = frame[:, :, ::-1]  

    # Detecta rostos no frame  
    face_locations = face_recognition.face_locations(rgb_frame)  
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  

    for face_encoding in face_encodings:  
        match = face_recognition.compare_faces([known_encoding], face_encoding)  

        if match[0]:  
            cv2.putText(frame, "Rosto reconhecido!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  

    # Mostra o vídeo com as informações  
    cv2.imshow("Video", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

video_capture.release()  
cv2.destroyAllWindows()  
