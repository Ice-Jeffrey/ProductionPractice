def gcd(a, b):
    mini = a 
    if a > b:
        mini = b
    
    for i in range(mini, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    
    return 1

def mcm(a, b):
    maxi = a
    if a < b:
        maxi = b
    
    for i in range(maxi, 1000000):
        if i % a == 0 and i % b == 0:
            return i

    return a * b

a, b = input().split()
a, b = int(a), int(b)

print(gcd(a,b), mcm(a, b))