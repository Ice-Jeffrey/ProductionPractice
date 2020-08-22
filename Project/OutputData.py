import numpy as np
import pandas as pd

def main():
    # 导入正样本训练集
    Positive = pd.read_csv('F:\Codes\ProductionPractice\OutputData\ExcelData5.csv')
    Positive.to_csv('Data/positive.csv', index=False)

    # 导入负样本训练集
    Negative = pd.read_csv('F:\\Codes\\ProductionPractice\\OutputData\\NotParticipateInfo.csv')
    falseList = []
    for index, item in enumerate(Negative[Negative['年份'] > 5].values):
        falseList.append(Negative.index[index])
    Negative.drop(index=falseList, inplace=True)
    Negative.to_csv('Data/negative.csv', index=False)

    # 读入测试集
    data1 = pd.read_csv('OutputData/35Info.csv')
    data2 = pd.read_csv('OutputData/46Info.csv')
    TestData = pd.concat([data1, data2], axis=0, ignore_index=False)
    TestData.to_csv('Data/testdata.csv', index=False)

    print('数据处理完成')

if __name__ == "__main__":
    main()