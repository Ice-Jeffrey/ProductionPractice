# 使用决策树对已有数据进行多分类

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def getTrainingData():
    # 读入正样本
    positive = pd.read_csv('Data/positive_training.csv')
    positive.drop(['学号'], axis=1, inplace=True)

    # 读入负样本
    negative = pd.read_csv('Data/NegativeTraining.csv')
    negative.drop(['学号'], axis=1, inplace=True)

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative

def getTestingData():
    data = pd.read_csv('Data/testing.csv')
    data.drop(['学号'], axis=1, inplace=True)
    return data

def main():
    # 从文件中读入训练集
    positive, negative = getTrainingData()
    
    # 从文件中读入测试集
    Testingdata = getTestingData()

    # 计算出需要模型的次数
    iter = negative.shape[0] // positive.shape[0]   # iter = 5

    for i in range(iter):
        # 获得需要的数据
        # data = pd.concat([positive, negative.iloc[i * 228: (i+1)*228, :]], axis=0)
        data = positive
        data = shuffle(data)

        # 得到X, y
        y = data['获奖类别']
        X = data.iloc[:, :-1]
        # X = data.iloc[:, :12]
        # print(X, y)

        # 分割训练集与测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # stratify=y)

        # 使用决策树模型对训练集进行拟合
        model = DecisionTreeClassifier(class_weight='balanced')
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        # print(predictions, end='\t')
        
        print(i, model.score(X_test, y_test))

        tests = model.predict(Testingdata.iloc[:, :-1])
        print(tests)
        
if __name__ == "__main__":
    main()