m, n = input().split()
m, n = float(m), int(n)

meters = 0
height = 0

for i in range(n):
    height = m / 2
    meters += m * 1.5
    m = m / 2

print("%.2f" % height, "%.2f" % (meters - m))