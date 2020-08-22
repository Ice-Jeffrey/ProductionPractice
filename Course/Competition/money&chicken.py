for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        if k % 3 == 0 and 5 * i + 3 * j + k / 3 == 100:
            print(i, j, k)