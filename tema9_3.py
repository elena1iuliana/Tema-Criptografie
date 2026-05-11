import math

def factorize(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def chinese_remainder_theorem(items):
    N = 1
    for _, m in items:
        N *= m
    result = 0
    for r, m in items:
        p = N // m
        result += r * pow(p, -1, m) * p
    return result % N

def pohlig_hellman(g, h, p):
    n = p - 1 
    factors = factorize(n)
    congruences = []

    for q, e in factors.items():
        x_q = 0
        gamma = pow(g, n // q, p)
        for i in range(e):
            exp = n // (q**(i + 1))
            h_i = pow(pow(g, -x_q, p) * h, exp, p)
            d = -1
            for val in range(q):
                if pow(gamma, val, p) == h_i:
                    d = val
                    break
            x_q += d * (q**i)
        
        congruences.append((x_q, q**e))

    return chinese_remainder_theorem(congruences)
p_test = 31 
g_test = 3
h_test = 26
print(f"Pohlig-Hellman: x = {pohlig_hellman(g_test, h_test, p_test)}")
