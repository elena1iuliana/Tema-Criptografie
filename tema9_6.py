import hashlib
import random
def sha256_hash(u1, u2, v):
    """Funcție hash simplă pentru Cramer-Shoup"""
    data = f"{u1}{u2}{v}".encode()
    return int(hashlib.sha256(data).hexdigest(), 16)
def cramer_shoup_keygen(p=4611686018427387847):
    q = (p - 1) // 2
    g1 = 2
    g2 = 3 
    x1, x2, y1, y2, z = [random.randint(1, q-1) for _ in range(5)]
    c = (pow(g1, x1, p) * pow(g2, x2, p)) % p
    d = (pow(g1, y1, p) * pow(g2, y2, p)) % p
    h = pow(g1, z, p)
    
    pub = (p, q, g1, g2, c, d, h)
    priv = (x1, x2, y1, y2, z)
    return pub, priv

def cs_encrypt(m, pub):
    p, q, g1, g2, c, d, h = pub
    r = random.randint(1, q-1)
    
    u1 = pow(g1, r, p)
    u2 = pow(g2, r, p)
    v = (m * pow(h, r, p)) % p
    
    alpha = sha256_hash(u1, u2, v)
    w = (pow(c, r, p) * pow(d, r * alpha, p)) % p
    
    return (u1, u2, v, w)

def cs_decrypt(cipher, pub, priv):
    p, q, g1, g2, c, d, h = pub
    x1, x2, y1, y2, z = priv
    u1, u2, v, w = cipher
    
    alpha = sha256_hash(u1, u2, v)
    test_w = (pow(u1, x1 + y1 * alpha, p) * pow(u2, x2 + y2 * alpha, p)) % p
    
    if w != test_w:
        raise ValueError("Eroare: Integritatea mesajului a fost compromisă!")
 
    m = (v * pow(u1, -z, p)) % p
    return m

pub, priv = cramer_shoup_keygen()
mesaj = 987654321
cifrat_cs = cs_encrypt(mesaj, pub)
decriptat_cs = cs_decrypt(cifrat_cs, pub, priv)
print(f"Cramer-Shoup: Original {mesaj} -> Decriptat {decriptat_cs}")
