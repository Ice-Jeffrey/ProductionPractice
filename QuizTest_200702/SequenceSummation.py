N = int(input())

a = [2, 3]
b = [1, 2]


sum = 0
for i in range(N):
    if i >= 2:
       a.append(a[i-1] + a[i-2])
       b.append(b[i-1] + b[i-2])

    sum += a[i] / b[i]

print("%.2f" % sum) 