'''
1: Випадково обираємо елiптичну криву (тобто параметри a, b), якщо обранi параме-
три задовольняють «посиленiй» умовi гладкостi, йдемо на крок 2.
2: Випадково обираємо точку цiєї елiптичної кривої P(x1, y1).
3: Нехай j = 2.
4: Обчислюємо точку Q = jP.
5: if при обчисленнях виникла помилка при пошуку оберненого then
6: зберегти значення d, обернений елемент до якого не вдалось обчислити.
7: if d < n then
8: d – шуканий нетривiальний дiльник числа n.
9: else d = n, повертаємось на крок 1 та обираємо нову елiптичну криву.
10: else j := j + 1.
'''

from math import gcd

def check(a, b, n):
    return gcd(4 * a ** 3 + 27 * b ** 2, n) == 1

def calc_fraction(up, down, m):
    res = gcd(down, m)
    if res != 1:
        print("d =", res)
        raise Exception("Error")
    print("calc", down, "^ -1 mod", m)
    return (up * pow(down, -1, m)) % m

def double_p(x, y, a, n):
    #value = ((3 * x ** 2 + a) * pow((2 * y) % n, -1, n)) % n
    value = calc_fraction((3 * x ** 2 + a) % n, (2 * y) % n, n)
    x4 = ((value) ** 2 - 2 * x) % n
    y4 = (-y + value * (x - x4)) % n
    return (x4, y4)

def sum_pq(x1, y1, x2, y2, n):
    value = calc_fraction((y1 - y2) % n, (x1 - x2) % n, n)
    x3 = (value ** 2 - x1 - x2) % n
    y3 = (-y1 + value * (x1 - x3)) % n
    return (x3, y3)

def Lenstra():
    a = 3
    b = 2
    n = 949
    
    print("a =", a, "b =", b, "n =", n)
    
    if not check(a, b, n):
        print("Incorrect a, b")
        return
    
    px = 15
    py2 = (px ** 3 + a * px + b) % n
    py = 1
    for py in range(n):
        if pow(py, 2, n) == py2:
            break
    
    print("P = (" + str(px) + "; " + str(py) + ")")
    
    qx, qy = px, py
    i = 2
    while True:
        print("i =", i)
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
    
Lenstra()
