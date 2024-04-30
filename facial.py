import cv2 # OpenCV library for computer vision
CascPath = "haarcascade_frontalface_default (1).xml" #archivo para la deteccion de rostros forntales ir a: https://github.com/opencv/opencv/tree/4.x/data/haarcascades
                                                     # descargo el archivo haarcascade_frontalface_default (1).xml y lo abro en visual studio

faceCasade = cv2.CascadeClassifier(CascPath) # aqui creo un objeto Cascadeclasiffier de Opencv, esto encapsula la información necesaria para realizar la deteccion de rostros utiliand el algoritmo de haar.

video_capture = cv2.VideoCapture(0) # incio la captura de video desde la camara el valor CERO es pra usar la camara predeterminada del sistema, si tengo varias camaras cambio el numero.

while True: # inicio un bucle infinito que captura continuamente los frames del video
    ret, frame = video_capture.read() # el valor red, india si la capturta ha sido exitosa, el frame es el frame capturado por la camara
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convertimos el frame capturado en una imagen en escala de grises, 'la detce funciona mejor en escala de grises.
    
    # codigo para hacer que nuestro programa detecte los rostros
    faces = faceCasade.detectMultiScale(
        
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
               
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2) # dibujo un rectangulo verde, con las coordenadas y el ancho. 
        
    cv2.imshow('video', frame)  # muestro el frame capturado en una ventana
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # esto es; si wl usuario presiona la tecla 'q' la ventana se cierra. rompe el bucle
        break
    
video_capture.release() # libera todos los recursos y la camara
cv2.destroyAllWindows() # cierra las ventanas
