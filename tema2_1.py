def rezolva_euclid_extins(a, b):
    b_cop =  b
    a, b = abs(a), abs(b)
    xa, xb = 1, 0
    ya, yb = 0, 1

    while b != 0:
        q = a // b
        r = a % b
        a, b = b, r
        xa, xb = xb, xa - q * xb
        ya, yb = yb, ya - q * yb
    x = xa if a >= 0 else -xa
    y = ya if b >= 0 else -ya
    cmmdc = a
    inv_a_mod_b = x % b_cop if (cmmdc == 1 and b_cop > 1) else None
    return {
        "cmmdc": cmmdc,
        "x": x,
        "y": y,
        "invers_modular": inv_a_mod_b,
    }
if __name__ == '__main__':
    rez1 = rezolva_euclid_extins(122, 343)
    print(f"Test 122 și 343: {rez1}")
    rez2 = rezolva_euclid_extins(12, 18)
    print(f"\nTest 12 și 18: {rez2}")