# 处理输入
m, n = input().split()
m, n = float(m), int(n)

# 进行计算
meters = 0
height = 0
for i in range(n):
    meters += m * 1.5
    height = m/2
    m = m/2

print("%.2f" % height, "%.2f" % (meters - m))