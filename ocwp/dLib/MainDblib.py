import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

logo = cv2.imread("logo1.png")
cv2.imshow("logo", logo)

imagenReconhecida = face_recognition.load_image_file("eu.jpg")
imagenReconhecida_encoding = face_recognition.face_encodings(imagenReconhecida)[0]


face_locations = []
face_encodings_filmadas = []
nome_das_faces = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

    if process_this_frame:
        #procurando todos os rostos e encodings na camera
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings_filmadas = face_recognition.face_encodings(small_frame, face_locations)

        nome_das_faces = []
        for face_encoding in face_encodings_filmadas:
            match = face_recognition.compare_faces([imagenReconhecida_encoding], face_encoding)
            name = "desconhecido"

            if match[0]:
                name = "Pedro H. Gomes"

            nome_das_faces.append(name)

    process_this_frame = not process_this_frame




    for (top, right, bottom, left), name in zip(face_locations, nome_das_faces):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4


        #desenhando um retangulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255),2)


        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0,255), cv2.RETR_FLOODFILL)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('reconhecedor, v1.0, 04-06-2017, Pedro H. Gomes - Luan Sousa', frame)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()