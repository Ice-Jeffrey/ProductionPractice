# 用途：对已有的正样本、负样本和测试集添加ACMER.site的相关信息

import numpy as np
import pandas as pd

def processData(data):
    acmers = pd.read_csv('OutputData/Acmers.csv')
    stuNos = list(acmers['stuNo'])

    features = [
        'acRating', 'cfRating', 'jskRating', 
        'acTimes', 'cfTimes', 'ncTimes', 'jskTimes', 
        'all_cf_aftersolve', 'correct_cf_aftersolve', 
        'all_ac_aftersolve', 'correct_ac_aftersolve'
    ]
    columns = data.columns[:-1]
    
    data.loc[:, features] = 0

    for index, item in enumerate(data.values):
        if item[0] in stuNos:
            print(index, item[0])
            data.loc[index, features] = acmers.loc[stuNos.index(item[0]), features]
    
    return data


def main():
    # 处理数据
    paths = [
        'Data/positive.csv',
        'Data/negative.csv',
        'Data/testdata.csv'
    ]

    for path in paths:
        data = pd.read_csv(path)
        data = processData(data)

        columns = list(data.columns)
        columns.remove('获奖类别')
        columns.append('获奖类别')
        
        data.to_csv(path[:-4] + '_acmer.csv', 
            index=False,
            columns=columns
        )
    
    print('处理完成')

if __name__ == "__main__":
    main()