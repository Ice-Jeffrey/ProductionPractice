# 编程语言映射的函数
def function1(x):
    if 'C/C++' in x:
        return 0
    elif 'Java' in x:
        return 1
    else:
        return 2
    
# 性别映射的函数
def function2(x):
    if x == '男':
        return 1
    else:
        return 0
    
# 专业映射的函数
def function3(x):
    if '计算机' in x:
        return 1
    else:
        return 0

# 定义一个对奖项进行映射的函数
def function4(x):
    if '一等奖' == x:
        return 0
    elif '二等奖' == x:
        return 1
    elif '三等奖' == x:
        return 2
    elif '优秀奖' == x:
        return 3
    else:
        return 4
    
# 定义一个对奖项级别进行映射的函数
def function5(x):
    if '省部级' == x:
        return 1
    elif '国家级' == x:
        return 0
    else:
        return 2