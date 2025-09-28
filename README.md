# Detector de Emociones con OpenCV, MediaPipe y Arduino

Este proyecto utiliza visión por computadora para detectar si una persona está **sonriendo** o **seria** en tiempo real, y muestra el resultado en una pantalla **LCD I2C** conectada a un Arduino.

## 📷 Visión General del Proyecto

- El script de **Python** usa la webcam y MediaPipe para analizar los puntos faciales.
- Calcula la distancia entre las comisuras de los labios para determinar si la persona está sonriendo.
- Envía un carácter ('A' o 'B') al Arduino mediante comunicación **Serial**.
- El **Arduino** recibe el carácter y actualiza el mensaje mostrado en la pantalla LCD:
  - `'A'` → "SMILING"
  - `'B'` → "SERIOUS"

---

## 📁 Archivos

- `detector_emociones.py`: Script principal en Python.
- `detector_arduino.ino`: Código para el Arduino con pantalla LCD.
- `README.md`: Documentación del proyecto (este archivo).

---

## ⚙️ Requisitos

### Python

- Python 3.7+
- Librerías:
  - `opencv-python`
  - `mediapipe`
  - `pyserial`

Instalación (recomendado con `pip`):

pip install opencv-python mediapipe pyserial'''

##Arduino

Arduino UNO o compatible.

Pantalla LCD I2C (16x2 o 20x4).

Librería: LiquidCrystal_I2C

Puedes instalar esta librería desde el Library Manager del IDE de Arduino.

🔌 Conexión de Hardware

LCD I2C conectado al Arduino:

SDA → A4

SCL → A5

Arduino conectado al PC vía USB.

🧠 Lógica del Código
Python (detector_emociones.py)

Captura el video desde la webcam.

Usa MediaPipe FaceMesh para detectar puntos faciales.

Calcula la distancia entre los puntos 61 y 306 (esquinas de la boca).

Si la distancia > 50 → sonrisa ('A')

Si la distancia ≤ 50 → serio ('B')

Envía el resultado por Serial al Arduino.

Arduino (detector_arduino.ino)

Inicializa la pantalla LCD I2C.

Escucha en el puerto Serial.

Si recibe 'A', muestra "SMILING" en la pantalla.

Si recibe cualquier otro carácter, muestra "SERIOUS".

▶️ Cómo Ejecutar

Cargar el código Arduino (detector_arduino.ino) en tu placa.

Asegúrate de que la pantalla LCD está correctamente conectada y mostrando el mensaje inicial.

Ejecuta el script de Python:

python detector_emociones.py


Observa cómo cambia el mensaje en la LCD dependiendo de tu expresión facial.

Pulsa q para salir.

📝 Notas

Asegúrate de cambiar el puerto COM en el script de Python según tu sistema:

arduino = serial.Serial('COM10',9600)


En Linux/MacOS, puede ser algo como /dev/ttyUSB0

📸 Captura de Pantalla (opcional)
## 🔧 Circuito

![Circuito del proyecto](docs/circuito.jpg)

## 📷 Resultados

### 😄 Sonriendo
![Rostro Sonriendo](docs/smile.jpg)

### 😐 Serio
![Rostro Serio](docs/sad.jpg)

### LCD mostrando "SMILING"
![LCD SMILING](images/lcdSmile.jpg)

### LCD mostrando "SERIOUS"
![LCD SERIOUS](images/lcdSerious.jpg)
