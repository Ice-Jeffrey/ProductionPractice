a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

sum = 0

for i in range(1, a+1):
    sum += i

for i in range(1, b+1):
    sum += i ** 2

for i in range(1, c+1):
    sum += 1/i

print("%.2f" % sum)