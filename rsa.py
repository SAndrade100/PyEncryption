import random

# Função para calcular o MDC
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o inverso modular
def mod_inverse(e, phi):
    m0, x0, x1 = phi, 0, 1
    while e > 1:
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Gerar um número primo pequeno para aprendizado
def generate_prime():
    while True:
        num = random.randint(100, 200)
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num

# Geração de chaves RSA
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:  # Evitar p == q
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:  # Encontrar 'e' coprimo com φ
        e += 2

    d = mod_inverse(e, phi)
    return (e, n), (d, n)  # Retorna chave pública e privada

# Criptografar
def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

# Descriptografar
def decrypt(encrypted_message, private_key):
    d, n = private_key
    return pow(encrypted_message, d, n)

# Teste
public_key, private_key = generate_keys()
message = 42

encrypted = encrypt(message, public_key)
decrypted = decrypt(encrypted, private_key)

print("Mensagem original:", message)
print("Mensagem criptografada:", encrypted)
print("Mensagem descriptografada:", decrypted)
