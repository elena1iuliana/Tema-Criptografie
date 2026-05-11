import math

def factorizare_fermat(n):
    if n % 2 == 0:
        return n // 2, 2
    if t * t == n:
        return t, t
    t += 1

    while True:
        s2 = t**2 - n
        s = math.isqrt(s2)
        if s * s == s2:
            a = t - s
            b = t + s
            return a, b
        
        t += 1

def testf(n_test):
    a, b = factorizare_fermat(n_test)
    print(f"Numărul {n_test}:")
    print(f"  t = {(a + b) // 2}, s = {(b - a) // 2}")
    print(f"  Factori: {a} * {b} = {n_test}")
    print("-" * 30)


 testf(6887)
 testf(10961)
 testf(40723)
