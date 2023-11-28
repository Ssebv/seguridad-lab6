import socket
from crypto_utils import *

def recibir_clave_publica(conn): # Función para recibir la clave pública del servidor
    clave_publica_data = conn.recv(4096) # Recibir clave pública
    # print(eval(clave_publica_data.decode()))
    return eval(clave_publica_data.decode()) # Convertir la clave pública a tupla 

def leer_y_cifrar_mensaje(public_key): # Función para leer y cifrar el mensaje de entrada
    with open('./mensajes/mensajeentrada.txt', 'r') as f:
        mensaje = f.read() # Leer mensaje de entrada
    return cifrar_rsa(mensaje.encode('utf-8'), public_key)

def main():
    host = "127.0.0.1"
    port = 65000

    with socket.create_connection((host, port)) as conn:
        print(f"Conectado al servidor en {host}:{port}")

        public_key = recibir_clave_publica(conn) # Recibir clave pública del servidor
        # print('Clave pública recibida del servidor.')

        mensaje_cifrado = leer_y_cifrar_mensaje(public_key)
        
        if mensaje_cifrado:
            conn.sendall(mensaje_cifrado)
            print("Mensaje cifrado y enviado al servidor.")
    
if __name__ == "__main__":
    main()
