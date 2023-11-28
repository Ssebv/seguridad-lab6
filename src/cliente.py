import socket
from crypto_utils import *

def recibir_clave_publica(conn):
    # Asumiendo que la clave pública se envía en un formato que se pueda reconstruir
    clave_publica_data = conn.recv(4096)
    return eval(clave_publica_data.decode())

def leer_y_cifrar_mensaje(public_key):
    with open('./mensajes/mensajeentrada.txt', 'r') as f:
        mensaje = f.read()
    return cifrar_rsa(mensaje.encode('utf-8'), public_key)

def main():
    host = "127.0.0.1"
    port = 65000

    with socket.create_connection((host, port)) as conn:
        print(f"Conectado al servidor en {host}:{port}")

        public_key = recibir_clave_publica(conn)
        print('Clave pública recibida del servidor.')

        mensaje_cifrado = leer_y_cifrar_mensaje(public_key)
        conn.sendall(mensaje_cifrado)
        print("Mensaje cifrado y enviado al servidor.")

if __name__ == "__main__":
    main()
