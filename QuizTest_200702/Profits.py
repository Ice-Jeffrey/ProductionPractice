l = int(input())

profit = 0

if l <= 1000000:
    profit = l * 0.1
elif l > 1000000 and l <= 2000000:
    profit = 100000 + (l - 1000000) * 0.075
elif l > 2000000 and l <= 4000000:
    profit = 175000 + (l - 2000000) * 0.05
elif l > 4000000 and l <= 6000000:
    profit = 275000 + (l - 4000000) * 0.03
elif l > 6000000 and l <= 10000000:
    profit = 335000 + (l - 6000000) * 0.015
elif l > 10000000:
    profit = 395000 + (l - 10000000) * 0.01

print(int(profit))
