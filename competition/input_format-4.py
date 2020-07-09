n = int(input())

for i in range(n):
    m, *s = input().split()
    m = int(m)
    sum = 0
    for j in range(m):
        sum += int(s[j])
    
    print(sum)
