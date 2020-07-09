string = ''

while True:
    temp = input()
    if temp[-1] == '#':
        string += temp[:-1]
        break
    else:
        string += temp

l = []
for i in range(26):
    l.append(0)

for c in string:
    if c.isalpha():
        num = ord(c) - ord('a')
        l[num] = l[num] + 1

for index, item in enumerate(l):
    print(chr(ord('a') + index), item)