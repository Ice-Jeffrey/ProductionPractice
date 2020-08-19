import numpy as np
import pandas as pd
from functions import *

def main():
    # 从表格中载入数据
    data1 = pd.read_excel('F:\\Codes\\ProductionPractice\\Data\\2013-2019年蓝桥杯国家级获奖记录.xlsx')
    data2 = pd.read_excel('F:\\Codes\\ProductionPractice\\Data\\2013-2019年蓝桥杯省部级获奖记录.xlsx')

    # 去掉缺失值
    data1.dropna()
    data2.dropna()

    # 去掉无用的特征
    data1 = data1.drop(['生源地', '数据是否有问题'], axis=1)
    data2 = data2.drop(['生源地', '数据是否有问题'], axis=1)

    # 将data2中学号的科学计数法改为字符串形式
    data2['学号'] = data2['学号'].apply(lambda x: str(x)[0:10])

    # 对缺失的学号数据进行处理
    is_null = []
    for index, item in enumerate(data2['学号']):
        if item == 'nan':
            is_null.append(index)
    data2 = data2.drop(index=is_null, axis=0)

    # 创建新特征年级
    data1['年级'] = data1['班级'].map(lambda x: int(x[2:4]) + 2000)
    data2['年级'] = data2['班级'].map(lambda x: int(x[2:4]) + 2000)

    # 根据获奖年份和年级算出学生的编程年份
    data1['编程年份'] = data1['年份'] - data1['年级']
    data2['编程年份'] = data2['年份'] - data2['年级']

    # 算出编程年份后去掉无用的信息
    data1 = data1.drop(['年级', '班级'], axis=1)
    data2 = data2.drop(['年级', '班级'], axis=1)

    # 转换科目名称
    data1['科目名称'] = data1['科目名称'].apply(function1)
    data2['科目名称'] = data2['科目名称'].apply(function1)

    # 转换性别
    data1['性别'] = data1['性别'].apply(function2)
    data2['性别'] = data2['性别'].apply(function2)

    # 转换专业
    data1['专业'] = data1['专业'].apply(function3)
    data2['专业'] = data2['专业'].apply(function3)

    # 重新映射获奖结果
    data1['奖励级别'] = data1['奖励级别'].map(function5)
    data2['奖项等级'] = data2['奖项等级'].map(function5)

    data1['奖项'] = data1['奖项'].map(function4)
    data2['奖项'] = data2['奖项'].map(function4)

    data1['获奖类别'] = data1['奖励级别'] * 4 + data1['奖项']
    data2['获奖类别'] = data2['奖项等级'] * 4 + data2['奖项']

    data1 = data1.drop(['奖励级别', '奖项'], axis=1)
    data2 = data2.drop(['奖项等级', '奖项'], axis=1)

    # print(data1.head(), '\n\n', data2.head())
    
    data = pd.concat([data1, data2], axis=0)
    data.index = [x for x in range(1, data.shape[0]+1)]
    print(data.head())
    data.to_csv('OutputData/ExcelData1.csv', index=None)

if __name__ == "__main__":
    main()