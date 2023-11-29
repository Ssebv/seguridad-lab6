import socket
from crypto_utils import *

def enviar_clave_publica(conn, public_key): # Función para enviar la clave pública al cliente
    conn.sendall(str(public_key).encode())

def recibir_mensaje_cifrado(conn):  # Función para recibir el mensaje cifrado del cliente
    mensaje_cifrado = conn.recv(4096) # Recibir mensaje cifrado
    return mensaje_cifrado 

def main():
    host = '127.0.0.1'
    port = 65000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Esperando conexiones en {host}:{port}...')
        conn, addr = s.accept()
        print(f'Conexión establecida con {addr}')

        try:
            with conn:
                # print('Generando par de claves RSA...')
                public_key, private_key = generar_clave_rsa() # Generar par de claves RSA
                enviar_clave_publica(conn, public_key) # Enviar clave pública al cliente

                mensaje_cifrado = recibir_mensaje_cifrado(conn) # Recibir mensaje cifrado del cliente
                mensaje_descifrado = descifrar_rsa(mensaje_cifrado, private_key) # Descifrar mensaje
                print("Mensaje recibido y descifrado:", mensaje_descifrado) # Imprimir mensaje descifrado

                with open('./mensajes/mensajerecibido.txt', 'w') as f:
                    f.write(mensaje_descifrado)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
