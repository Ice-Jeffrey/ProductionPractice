while True:
    a, b = input().split()
    a, b = str(a), str(b)

    for j in range(len(a)):
        temp = a[1:] + a[0]
        if temp == b:
            print("Yes")
            break
        a = temp
    else:
        print("No")