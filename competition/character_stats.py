s = str(input())

letter = 0
space = 0
digit = 0
others = 0

for c in s:
    if c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    elif c.isalpha():
        letter += 1
    else:
        others += 1

print(letter, digit, space, others)