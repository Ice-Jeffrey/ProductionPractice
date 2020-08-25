# 使用决策树对已有数据进行多分类

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

from GetData import *

def model_with_negative():
    print('带有负样本的模型')

    # 从文件中读入训练集
    positive, negative = getNormalData()
    
    # 从文件中读入测试集
    Testingdata = getNormalTesting()

    # 计算出需要模型的次数
    iter = negative.shape[0] // positive.shape[0]   # iter = 5

    accuracy_list = {}
    for i in range(iter):
        # 获得需要的数据
        data = pd.concat([positive, negative.iloc[i * 228: (i+1)*228, :]], axis=0)
        data = shuffle(data)

        # 得到X, y
        y = data['获奖类别']
        X = data.iloc[:, :-1]

        # 分割训练集与测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

        # 使用DecisionTree模型对训练集进行拟合
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        test = model.predict(Testingdata.iloc[:, :-1])
        
        print("第{}个模型，准确率：{}\n预测结果：{}".format(i, accuracy_score(predictions, y_test), test))

        # 进行决策树的可视化
        dot_data = export_graphviz(
            model, filled=True, 
            feature_names=X.columns,
            out_file=None
        )
        graph = graph_from_dot_data(dot_data)
        graph.write_png('Visualization/with_negative_tree' + str(i) + '.png')   

    print("训练结束\n")

def model_with_only_positive():
    print('只有正样本的训练')
    # 从文件中读入训练集
    positive, negative = getNormalData()
    
    # 从文件中读入测试集
    Testingdata = getNormalTesting()
    
    # 获得需要的数据
    data = positive
    data = shuffle(data)

    # 得到X, y
    y = data['获奖类别']
    X = data.iloc[:, :-1]

    # 分割训练集与测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # 进行标准化
    scaler = StandardScaler().fit(X_train)
    Standardized_X_train = scaler.transform(X_train)
    Standardized_X_test = scaler.transform(X_test)

    scaler = StandardScaler().fit(Testingdata.iloc[:, :-1])
    Standardized_Testing = scaler.transform(Testingdata.iloc[:, :-1])

    # 使用DecisionTree模型对训练集进行拟合
    model = DecisionTreeClassifier()
    model.fit(Standardized_X_train, y_train)
    predictions = model.predict(Standardized_X_test)

    test = model.predict(Standardized_Testing)
    
    print("准确率：{}\n预测结果：{}".format(accuracy_score(predictions, y_test), test)) 

    # 进行决策树的可视化
    dot_data = export_graphviz(
        model, filled=True, 
        feature_names=X.columns,
        out_file=None
    )
    graph = graph_from_dot_data(dot_data)
    graph.write_png('Visualization/only_positive_tree.png')  

    print("训练结束\n")  

def model_with_ld_positive():
    print('降维后只有正样本的训练')
    # 从文件中读入训练集
    positive, negative = getLowerDimensionData()
    
    # 从文件中读入测试集
    Testingdata = getLowerDimensionTesting()
    
    # 获得需要的数据
    data = positive
    data = shuffle(data)

    # 得到X, y
    y = data['获奖类别']
    X = data.iloc[:, :-1]

    # 分割训练集与测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # 进行标准化
    scaler = StandardScaler().fit(X_train)
    Standardized_X_train = scaler.transform(X_train)
    Standardized_X_test = scaler.transform(X_test)

    scaler = StandardScaler().fit(Testingdata.iloc[:, :-1])
    Standardized_Testing = scaler.transform(Testingdata.iloc[:, :-1])

    # 使用DecisionTree模型对训练集进行拟合
    model = DecisionTreeClassifier()
    model.fit(Standardized_X_train, y_train)
    predictions = model.predict(Standardized_X_test)

    test = model.predict(Standardized_Testing)
    
    print("准确率：{}\n预测结果：{}".format(accuracy_score(predictions, y_test), test)) 

    # 进行决策树的可视化
    dot_data = export_graphviz(
        model, filled=True, 
        feature_names=X.columns,
        out_file=None
    )
    graph = graph_from_dot_data(dot_data)
    graph.write_png('Visualization/ld_positive_tree.png')  

    print("训练结束\n")  

def main():
    model_with_negative()
    model_with_only_positive()   
    model_with_ld_positive()
        
        
if __name__ == "__main__":
    main()

# def main():
#     # 从文件中读入训练集
#     positive, negative = getTrainingData()
    
#     # 从文件中读入测试集
#     Testingdata = getTestingData()

#     # 计算出需要模型的次数
#     iter = negative.shape[0] // positive.shape[0]   # iter = 5

#     for i in range(iter):
#         # 获得需要的数据
#         # data = pd.concat([positive, negative.iloc[i * 228: (i+1)*228, :]], axis=0)
#         data = positive
#         data = shuffle(data)

#         # 得到X, y
#         y = data['获奖类别']
#         X = data.iloc[:, :-1]
#         # X = data.iloc[:, :12]
#         # print(X, y)

#         # 分割训练集与测试集
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#         # 进行标准化
#         scaler = StandardScaler().fit(X_train)
#         Standardized_X_train = scaler.transform(X_train)
#         Standardized_X_test = scaler.transform(X_test)

#         scaler = StandardScaler().fit(Testingdata.iloc[:, :-1])
#         Standardized_Testing = scaler.transform(Testingdata.iloc[:, :-1])

#         # 使用决策树模型对训练集进行拟合
#         model = DecisionTreeClassifier(class_weight='balanced')
#         model.fit(Standardized_X_train, y_train)
        
#         print(i, model.score(Standardized_X_test, y_test))

#         tests = model.predict(Standardized_Testing)
#         print(tests)


#         # 进行决策树的可视化
#         dot_data = export_graphviz(
#             model, filled=True, 
#             feature_names=X.columns,
#             out_file=None
#         )
#         graph = graph_from_dot_data(dot_data)
#         graph.write_png('Visualization/tree' + str(i) + '.png')
        
# if __name__ == "__main__":
#     main()