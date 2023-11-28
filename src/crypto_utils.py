from Crypto.Util.number import getPrime, inverse
import random

def generar_clave_rsa(bits=2048):
    # Implementar la generación de claves RSA.
    # Deberás generar dos números primos grandes y calcular n = p * q y phi(n) = (p-1)(q-1).
    # Luego, elige e tal que 1 < e < phi(n) y mcd(e, phi(n)) = 1. d será el inverso multiplicativo de e módulo phi(n).
    # La clave pública será (e, n) y la clave privada (d, n).
    # Paso 1: Generar dos primos p y q
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    
    # Paso 2: Calcular n
    n = p * q
    
    # Paso 3: Calcular phi(n)
    phi = (p - 1) * (q - 1)
    
    # Paso 4: Elegir e
    e = random.randrange(1, phi)
    g = mcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = mcd(e, phi)
    
    # Paso 5: Calcular d
    d = inverse(e, phi)
    
    # La clave pública es (e, n) y la privada es (d, n)
    return ((e, n), (d, n))

def mcd(a, b):
    # Función para calcular el máximo común divisor usando el algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def cifrar_rsa(mensaje, clave_publica):
    # Convertir el mensaje en un número m
    m = int.from_bytes(mensaje, 'big')
    e, n = clave_publica

    # Cifrar usando la clave pública (e, n): c = m^e mod n
    c = pow(m, e, n)
    return c.to_bytes((c.bit_length() + 7) // 8, 'big')

def descifrar_rsa(mensaje_cifrado, clave_privada):
    c = int.from_bytes(mensaje_cifrado, 'big')
    d, n = clave_privada

    # Descifrar usando la clave privada (d, n): m = c^d mod n
    m = pow(c, d, n)
    mensaje = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')
    return mensaje

