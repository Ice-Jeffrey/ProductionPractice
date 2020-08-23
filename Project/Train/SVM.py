# 使用svm对已有数据进行多分类

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.utils import shuffle
from Onehot import onehot

def getData():
    # 读入正样本
    positive = pd.read_csv('Data/positive_acmer.csv')
    # 读入负样本
    negative = pd.read_csv('Data/negative_acmer.csv')

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative



def main():
    # 从文件中读入数据
    positive, negative = getData()

    # 计算出需要模型的次数
    iter = negative.shape[0] // positive.shape[0]

    for i in range(iter):
        print(iter)


if __name__ == "__main__":
    main()