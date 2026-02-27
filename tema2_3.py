def phi_euler(n):
    n = abs(n)
    if n == 0: return 0
    if n == 1: return 1
    rez = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            rez -= rez // p
        p += 1
    if n > 1:
        rez-= rez // n
    return rez
if __name__ == '__main__':
    numar_mare = 1234567890123456789
    print(f"phi({numar_mare}) = {phi_euler(numar_mare)}")
    print(f"phi(13) = {phi_euler(13)}") 