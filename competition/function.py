def function(x):
    if x < 1:
        return x
    elif x >= 1 and x < 10:
        return 2 * x - 1
    elif x >= 10:
        return 3 * x - 11

x = int(input())
y = function(x)
print(y)