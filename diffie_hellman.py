import random

#Geração de número primo grande (simplificado para experimento)
def generate_prime():
    while True:
        num = random.randint(1, 200000)
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num
        
#Implementação do Diffie-Hellman
def diffie_hellman():
    p = generate_prime()
    g = random.randint(2, p - 1)
    print(f"Primo público (p): {p}")
    print(f"Gerador público (g): {g}")
    
    private_a = random.randint(2, p - 1)
    private_b = random.randint(2, p - 1)
    
    public_a = pow(g, private_a, p)
    public_b = pow(g, private_b, p)
    print(f"Chave pública de A: {public_a}")
    print(f"Chave pública de B: {public_b}")
    
    shared_secret_a = pow(public_b, private_a, p)
    shared_secret_b = pow(public_a, private_b, p)

    print(f"Chave secreta calculada por A: {shared_secret_a}")
    print(f"Chave secreta calculada por B: {shared_secret_b}")

    assert shared_secret_a == shared_secret_b, "As chaves secretas não coincidem!"
    print("Chave secreta compartilhada:", shared_secret_a)
    
diffie_hellman()