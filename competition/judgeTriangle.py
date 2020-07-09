a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a + b > c and b + c > a and a + c > b:
    if a == b and b == c:
        print('DB')
    elif a == b or b == c:
        print('DY')
    elif a < b < c:
        print('ZJ')
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print('PT')
else:
    print('ERROR')