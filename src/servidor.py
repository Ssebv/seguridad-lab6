import socket
from crypto_utils import *

def enviar_clave_publica(conn, public_key):
    # Enviar la clave pública en un formato que el cliente pueda reconstruir
    conn.sendall(str(public_key).encode())

def recibir_mensaje_cifrado(conn):
    mensaje_cifrado = conn.recv(4096)
    return mensaje_cifrado

def main():
    host = '127.0.0.1'
    port = 65000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        print(f'Conexión establecida con {addr}')

        try:
            with conn:
                print('Generando par de claves RSA...')
                public_key, private_key = generar_clave_rsa()
                enviar_clave_publica(conn, public_key)

                mensaje_cifrado = recibir_mensaje_cifrado(conn)
                mensaje_descifrado = descifrar_rsa(mensaje_cifrado, private_key)
                print("Mensaje recibido y descifrado:", mensaje_descifrado)

                # Guardar el mensaje descifrado en un archivo
                with open('mensajerecibido.txt', 'w') as f:
                    f.write(mensaje_descifrado)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
