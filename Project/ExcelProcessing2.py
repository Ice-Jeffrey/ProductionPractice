import numpy as np
import pandas as pd


def main():
    # 加载数据
    data = pd.read_csv("F:\Codes\ProductionPractice\OutputData\ExcelData.csv")

    # 向data中添加新的特征
    data['国家级一等奖'] = 0
    data['国家级二等奖'] = 0
    data['国家级三等奖'] = 0
    data['国家级优秀奖'] = 0
    data['省部级一等奖'] = 0
    data['省部级二等奖'] = 0
    data['省部级三等奖'] = 0
    data['省部级优秀奖'] = 0

    # 创建一个列表对奖项的结果进行映射
    tempList = [
        '国家级一等奖',
        '国家级二等奖',
        '国家级三等奖',
        '国家级优秀奖',
        '省部级一等奖',
        '省部级二等奖',
        '省部级三等奖',
        '省部级优秀奖'
    ]
    
    # 对每条数据统计曾经的获奖情况
    for index, item in enumerate(data.values):
        # 筛选出该学生之前的获奖数据
        tempdata = data[data['年份'] < item[5]]
        tempdata = tempdata[tempdata['考生姓名'] == item[0]]

        # 若该学生之前有获奖记录
        if tempdata.shape[0] > 0:
            # 遍历获奖类别进行修改
            for tempitem in tempdata['获奖类别']:
                data.loc[index, tempList[tempitem]] += 1

    data.to_csv('OutputData/ExcelData2.csv', index=None)
    print("已导出文件")

if __name__ == "__main__":
    main()