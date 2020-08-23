import numpy as np
import pandas as pd

# 全局变量，选择要去掉的特征
drop = [
    '学号', '考生姓名', '年份', '科目名称', '性别',
    'acRating', 'jskRating', 
    'acTimes', 'ncTimes', 'jskTimes',
    'all_ac_aftersolve', 'correct_ac_aftersolve' 
]

def dataProcess1():
    # 处理训练数据的年份
    data = pd.read_csv('OutputData/testoutput_data.csv')
    
    # 修改年份
    for index, item in enumerate(data.values):
        inyear = int(str(item[0])[0:4])
        data.loc[index, '编程年份'] = 2020 - inyear
        data.loc[index, '专业'] = 1

    data.drop(drop[1:], axis=1, inplace=True)
    data.to_csv('Data/Testing.csv', index=False)

def dataProcess2():
    data = pd.read_csv('OutputData\positive_output_data.csv')
    data.drop(drop, axis=1, inplace=True)
    data.to_csv('Data/PositiveTraining.csv', index=None)

def dataProcess3():
    data = pd.read_csv('OutputData/negative_acmer.csv')
    data.drop(drop, axis=1, inplace=True)
    data.to_csv('Data/NegativeTraining.csv', index=False)

def main():
    dataProcess1()
    dataProcess2()
    dataProcess3()

if __name__ == "__main__":
    main()