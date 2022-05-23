from math import gcd

def check(a, b, n):
    return gcd(4 * a ** 3 + 27 * b ** 2, n) == 1

def calc_fraction(up, down, m):
    res = gcd(down, m)
    if res != 1:
        print("d = " + str(res))
        raise Exception("gcd != 1")
    print("calc " + str(down) + "^-1 mod " + str(m))
    return (up * pow(down, -1, m)) % m

def double_p(x, y, a, n):
    value = calc_fraction((3 * x ** 2 + a) % n, (2 * y) % n, n)
    x4 = ((value) ** 2 - 2 * x) % n
    y4 = (-y + value * (x - x4)) % n
    return (x4, y4)

def sum_pq(x1, y1, x2, y2, n):
    value = calc_fraction((y1 - y2) % n, (x1 - x2) % n, n)
    x3 = (value ** 2 - x1 - x2) % n
    y3 = (-y1 + value * (x1 - x3)) % n
    return (x3, y3)

def Lenstra(a, b, n):
    if not check(a, b, n):
        print("incorrect a, b")
        return
    px = 2
    py2 = (px ** 3 + a * px + b) % n
    py = 1
    for py in range(n):
        if pow(py, 2, n) == py2:
            break
    print("P = (" + str(px) + "; " + str(py) + ")")
    qx, qy = px, py
    i = 2
    while True:
        print("i = " + str(i))
        try:
            if i == 2:
                qx, qy = double_p(qx, qy, a, n)
            else:
                qx, qy = sum_pq(qx, qy, px, py, n)
        except Exception as error:
            print("if d == n:   try again   else:   beer")
            break
        print("Q = (" + str(qx) + "; " + str(qy) + ")")
        print()
        i += 1

Lenstra(2, 4, 949)
