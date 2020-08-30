import pandas as pd
from sklearn.utils import shuffle

# 读入正常样本的函数
def getNormalData():
    # 读入正样本
    positive = pd.read_csv('Data/positive_training.csv')
    positive.drop(['学号'], axis=1, inplace=True)

    # 读入负样本
    negative = pd.read_csv('Data/negative_training.csv')
    negative.drop(['学号'], axis=1, inplace=True)

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative

# 读入降维后的样本
def getLowerDimensionData():
    # 读入正样本
    positive = pd.read_csv('Data/positive_training_ld.csv')
    positive.drop(['学号'], axis=1, inplace=True)

    # 读入负样本
    negative = pd.read_csv('Data/negative_training_ld.csv')
    negative.drop(['学号'], axis=1, inplace=True)

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative

# 读入正常测试集
def getNormalTesting():
    data = pd.read_csv('Data/testing_output.csv')
    data.drop(['学号'], axis=1, inplace=True)
    return data

# 读入正常测试集
def getLowerDimensionTesting():
    data = pd.read_csv('Data/testing_output_ld.csv')
    data.drop(['学号'], axis=1, inplace=True)
    return data