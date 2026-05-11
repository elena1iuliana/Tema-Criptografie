import random

def simbol_jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0
    a = a % n
    rezultat = 1
    
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                rezultat = -rezultat
                a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            rezultat = -rezultat
        a = a % n
        
    if n == 1:
        return rezultat
    return 0

def solovay_strassen(n, k=10):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    for _ in range(k):
        b = random.randint(2, n - 1)
        exp = (n - 1) // 2
        x = pow(b, exp, n)
        s = simbol_jacobi(b, n)
        if s == 0 or x != (s % n):
            return False
    return True
n_test = 35
este_prim = solovay_strassen(n_test)
print(f"Numărul {n_test} este prim? {'DA' if este_prim else 'NU (Compus)'}")
print(f"Simbolul Jacobi (91/103): {simbol_jacobi(91, 103)}")
print(f"Simbolul Jacobi (109/385): {simbol_jacobi(109, 385)}")
