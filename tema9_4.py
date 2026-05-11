import random
from math import gcd
def L_func(x, p):
    return (x - 1) // p

def okamoto_uchiyama_keygen(bits=512):
    p = 3037000499 
    q = 3037000507 
    n = (p**2) * q
    
    while True:
        g = random.randint(2, n - 1)
        if pow(g, p - 1, p**2) != 1:
            break
    h = pow(g, n, n)
    public_key = (n, g, h)
    private_key = (p, q)
    return public_key, private_key

def okamoto_uchiyama_encrypt(m, public_key):
    n, g, h = public_key
    r = random.randint(2, n - 1)
    c = (pow(g, m, n) * pow(h, r, n)) % n
    return c

def okamoto_uchiyama_decrypt(c, public_key, private_key):
    n, g, h = public_key
    p, q = private_key
    cp = c % (p**2)
    num = L_func(pow(cp, p - 1, p**2), p)
    den = L_func(pow(g, p - 1, p**2), p)
    inv_den = pow(den, -1, p)
    m = (num * inv_den) % p
    return m
pub, priv = okamoto_uchiyama_keygen()
mesaj = 123456
criptat = okamoto_uchiyama_encrypt(mesaj, pub)
decriptat = okamoto_uchiyama_decrypt(criptat, pub, priv)

print(f"Okamoto-Uchiyama:")
print(f"  Mesaj original: {mesaj}")
print(f"  Mesaj decriptat: {decriptat}")
