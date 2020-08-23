# 使用svm对已有数据进行多分类

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def getData():
    drop = [
        '学号', '考生姓名', '年份', '科目名称',
        'acRating', 'jskRating', 
        'acTimes', 'ncTimes', 'jskTimes',
        'correct_cf_aftersolve', 'all_ac_aftersolve', 'correct_ac_aftersolve' 
    ]

    # 读入正样本
    positive = pd.read_csv('Data/positive_acmer.csv')
    positive.drop(drop, inplace=True, axis=1)

    # 读入负样本
    negative = pd.read_csv('Data/negative_acmer.csv')
    negative.drop(drop, inplace=True, axis=1)
    negative['获奖类别'] = 9

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative


def main():
    # 从文件中读入数据
    positive, negative = getData()

    # 计算出需要模型的次数
    iter = negative.shape[0] // positive.shape[0]

    for i in range(iter):
        # 获得需要的数据
        data = pd.concat([positive, negative.iloc[i * 228: (i+1)*228, :]], axis=0)
        data = shuffle(data)

        # 得到X, y
        y = data['获奖类别']
        X = data.iloc[:, :-1]
        # print(X, y)

        # 分割训练集与测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

        # 使用svc模型对训练集进行拟合
        svmModel = svm.SVC(kernel='linear', random_state=1, gamma=0.20, C=1.0)    ##较小的gamma有较松的决策边界
        svmModel.fit(X_train, y_train)

        predictions = svmModel.predict(X_test)
        print(predictions, end='\t')
        print(accuracy_score(predictions, y_test))
        


if __name__ == "__main__":
    main()