def splitIntoDigit(x):   
    c = x % 10
    b = (x - c) / 10 % 10
    a = (x - 10 * b - c) / 100
    return a, b, c


def main():
    for i in range(100, 1000):
        a, b, c = splitIntoDigit(i)
        if i == a ** 3 + b ** 3 + c ** 3:
            print(i)

if __name__ == "__main__":
    main()