import random

def is_quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

def goldwasser_micali_keygen(bits=256):
    p = 104729 
    q = 104723
    n = p * q
    while True:
        x = random.randint(2, n - 1)
        if (not is_quadratic_residue(x, p)) and (not is_quadratic_residue(x, q)):
            break
    return (n, x), (p, q)
def gm_encrypt(message_bits, public_key):
    n, x = public_key
    cipher = []
    for bit in message_bits:
        r = random.randint(2, n - 1)
        # c = (r^2 * x^bit) mod n
        c = (pow(r, 2, n) * pow(x, bit, n)) % n
        cipher.append(c)
    return cipher
def gm_decrypt(cipher, private_key):
    p, q = private_key
    message = []
    for c in cipher:
        if is_quadratic_residue(c, p):
            message.append(0)
        else:
            message.append(1)
    return message
pub, priv = goldwasser_micali_keygen()
mesaj_bits = [1, 0, 1, 1, 0]
cifrat = gm_encrypt(mesaj_bits, pub)
decriptat = gm_decrypt(cifrat, priv)
print(f"Goldwasser-Micali: Original {mesaj_bits} -> Decriptat {decriptat}")
