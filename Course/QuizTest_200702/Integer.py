integer = input()

# 输出字符串长度
print(len(integer))

# 输出各个数字
string = ''
for digit in integer:
    string += digit + ' '
print(string)

# 逆序输出数字
string = ''
L = list(integer)
L.reverse()
for digit in L:
    string += digit
print(string)