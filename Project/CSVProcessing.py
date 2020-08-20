import numpy as np
import pandas as pd 

def main():
    # 载入csv文件
    data = pd.read_csv('F:\Codes\ProductionPractice\OutputData\ExcelData4.csv')
    temp = data['获奖类别'].value_counts()
    # print(temp, type(temp))

    # 开始进行数据替换
    for i in temp.index:
        print('正在处理获奖类别为', i, '的异常数据')

        tempData = data[data['获奖类别'] == i]

        # 得到正常数据的中位数
        tempData1 = tempData[tempData['OJ提交数'] != 0]
        Submit = tempData1['OJ提交数'].describe()['50%']
        AC = tempData1['OJ正确数'].describe()['50%']

        # 得到异常数据
        tempData2 = tempData[tempData['OJ提交数'] == 0]
        
        if tempData2.shape[0] > 0:
            # 对异常数据进行替换
            for idx in tempData2.index:
                data.loc[idx, ['OJ提交数']] = Submit
                data.loc[idx, ['OJ正确数']] = AC
                data.loc[idx, ['OJ准确率']] = AC / Submit
    
    # print(data)

    # 将数据导出为CSV文件
    data.to_csv(
        'OutputData/ExcelData5.csv', 
        columns=['学号', '考生姓名', '科目名称', '性别', '专业', '年份', '编程年份', 
                '国家级一等奖', '国家级二等奖', '国家级三等奖', '国家级优秀奖',
                '省部级一等奖', '省部级二等奖', '省部级三等奖', '省部级优秀奖', 
                '获奖类别'], 
        index=False
    )
    print("已导出文件")

if __name__ == "__main__":
    main()