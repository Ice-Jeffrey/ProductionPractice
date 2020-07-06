def getFactors(x):
    l = [1]
    for i in range(2, x//2):
        if x % i == 0:
            l.append(i)
            l.append(x//i)

    return sorted(list(set(l)))

def main():
    N = int(input())

    for i in range(2, N+1):
        factors = getFactors(i)
        
        sum = 0
        for factor in factors:
            sum += factor
        if sum == i:
            string = ''
            for factor in factors:
                string += str(factor) + ' '
            print(i, 'its factors are', string)
        
if __name__ == "__main__":
    main()
