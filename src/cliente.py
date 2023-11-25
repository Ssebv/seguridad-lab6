import socket
from crypto_utils import *

def cifrar_mensaje(public_key, mensaje):
    # Función para cifrar el mensaje usando la clave pública RSA
    pass

def main():
    host = "127.0.0.1"
    port = 65000

    with socket.create_connection((host, port)) as conn:
        print(f"Conectado al servidor en {host}:{port}")

        public_key = recibir_clave_publica(conn)
        print('Clave pública recibida del servidor.')

        mensaje = 'Mensaje a cifrar'  # Este mensaje podría venir de un archivo 'mensajeentrada.txt'
        mensaje_cifrado = cifrar_mensaje(public_key, mensaje)
        conn.sendall(mensaje_cifrado)
        print("Mensaje cifrado y enviado al servidor.")

if __name__ == "__main__":
    main()
