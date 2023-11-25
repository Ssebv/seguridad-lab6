import socket
from crypto_utils import *

def generador_claves_rsa():
    # Esta función deberá generar un par de claves RSA y retornarlas
    pass

def recibir_mensaje_cifrado(conn):
    # Función para recibir un mensaje cifrado del cliente
    pass

def descifrar_mensaje(private_key, mensaje_cifrado):
    # Función para descifrar el mensaje usando la clave privada RSA
    pass

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
                public_key, private_key = generador_claves_rsa()
                enviar_clave_publica(conn, public_key)

                mensaje_cifrado = recibir_mensaje_cifrado(conn)
                mensaje_descifrado = descifrar_mensaje(private_key, mensaje_cifrado)
                print("Mensaje recibido y descifrado:", mensaje_descifrado)

                # Guardar el mensaje descifrado en un archivo
                with open('mensajerecibido.txt', 'w') as f:
                    f.write(mensaje_descifrado)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
