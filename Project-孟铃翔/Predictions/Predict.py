import numpy as np
import pandas as pd
import json

def str_to_list(s):
    l = []
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            l.append(ord(s[i]) - ord('0'))
    # print(l)
    return l

def getData(path):
    data = pd.read_csv(path)
    l1 = data['降维前准确率'].tolist()
    l2 = data['降维后准确率'].tolist()

    if max(l1) < max(l2):
        index = l2.index(max(l2))
        return data.loc[index, '降维后预测值']
    else:
        index = l1.index(max(l1))
        return data.loc[index, '降维前预测值']


def function(i):
    prizes = [
        '国家级一等奖',
        '国家级二等奖',
        '国家级三等奖',
        '国家级优秀奖',
        '省部级一等奖',
        '省部级二等奖',
        '省部级三等奖',
        '省部级优秀奖'
    ]

    return prizes[i]

def main():
    data = pd.read_excel('F:/Codes/ProductionPractice/Project/Data/2020年蓝桥杯报名数据.xlsx')
    
    data1 = str_to_list(getData('Results/AdaBoostWithOnlyPositive.csv'))
    data2 = str_to_list(getData('Results/DecisionTreeWithOnlyPositive.csv'))
    data3 = str_to_list(getData('Results/GDBTWithOnlyPositive.csv'))
    data4 = str_to_list(getData('Results/KNNWithOnlyPositive.csv'))
    data5 = str_to_list(getData('Results/LogisticRegressionWithOnlyPositive.csv'))
    data6 = str_to_list(getData('Results/SVMWithOnlyPositive.csv'))

    temp = pd.read_csv('Results/NeuralNetworkResult.csv')
    list1 = temp['准确率'].tolist()
    list2 = temp['预测结果'].tolist()
    index = list1.index(max(list1))
    data7 = str_to_list(list2[index])

    for i in range(len(data1)):
        x = data1[i] + data2[i] + data3[i] + data4[i] + data5[i] + data6[i] + data7[i]
        x = round(x / 7)
        data.loc[i, '2020年蓝桥杯奖项预测'] = function(x)
    data.to_csv('Predictions/Result.csv', index=False, encoding='gbk')

if __name__ == "__main__":
    main()