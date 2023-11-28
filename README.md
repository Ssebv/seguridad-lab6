# Cliente-Servidor RSA

Se implementa un sistema cliente-servidor que utiliza el algoritmo RSA para la sincronización de claves públicas y privadas. El cliente cifra un mensaje utilizando la clave pública del servidor, y el servidor lo descifra usando su clave privada.

## Estructura

- `server.py`: Implementa el servidor en Python.
- `client.py`: Implementa el cliente en Python.
- `crypto_utils.py`: Contiene las funciones de generación de claves, cifrado y descifrado RSA.
- `mensajeentrada.txt`: Archivo de texto que contiene el mensaje a ser cifrado por el cliente.
- `mensajerecibido.txt`: Archivo donde se guarda el mensaje descifrado por el servidor.

### Instalar Dependencias Python

Asegúrate de tener instalado Python y luego instala las dependencias necesarias:

### Instalar Dependencias Python
```bash
pip install -r requirements.txt
```
### Ejecución
Se debe ejecutar primero el servidor y luego el cliente en terminales separadas.

#### Ejecutar el Servidor
```bash
python3 server.py
```
#### Ejecutar el Cliente
```bash
python3 client.py
```
### Verificar Resultados

El mensaje cifrado por el cliente y luego descifrado por el servidor se guardará en el archivo mensajerecibido.txt.

### Autores
Sebastian Allende
Gianfranco Astorga