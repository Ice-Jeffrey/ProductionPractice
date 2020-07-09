while True:
    a, b = input().split()
    a, b = int(a), int(b)

    if a == 11 and 11 - b >= 2:
        print("Game Over")
    elif b == 11 and 11 - a >= 2:
        print("Game Over")
    else:
        if a > 10 and b > 10:
            if a - b == 2:
                print("Game Over")
            elif b - a == 2:
                print("Game Over")
            else:
                if a == b:
                    print("A")
                else:
                    print("B")
        else:
            if (a + b) % 4 <= 1:
                print('A') 
            else:
                print("B")
