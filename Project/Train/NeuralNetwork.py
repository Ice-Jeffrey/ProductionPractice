import numpy as np
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

import paddle.fluid as fluid
import paddle
from paddle.fluid.dygraph.nn import Linear
from paddle.fluid.dygraph.nn import Embedding

# 自定义神经网络模型
class Model(fluid.dygraph.Layer):
    # 先定义网络的结构
    def __init__(self, num_classes=8):
        super(Model, self).__init__()
        self.fc1 = Linear(input_dim=10, output_dim=32, act='relu') # 输入层和隐藏层的连接，隐藏层使用Sigmoid作为激活函数
        self.fc2 = Linear(input_dim=32, output_dim=16, act='relu') # 第一个隐藏层和第二个隐藏层之间的连接
        self.fc3 = Linear(input_dim=16, output_dim=num_classes, act='sigmoid') # 隐藏层和输出层的连接，输出层不使用激活函数

    # 网络的前向计算过程
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

# 定义训练神经网络的函数
def train(model, x_train, y_train):
    print('start training ... ')
    model.train()
    epoch_num = 600        # 定义训练100轮
    opt = fluid.optimizer.RMSPropOptimizer(learning_rate=0.02, parameter_list=model.parameters()) #定义优化器为Momentum，学习率为0.01

    # 由于数据量较小，在训练时不设定batch，直接逐轮训练
    for epoch in range(epoch_num):
        # 调整输入数据形状和类型
        x_data = np.array(x_train, dtype='float32').reshape(-1, x_train.shape[1])
        y_data = np.array(y_train, dtype='int64').reshape(-1, 1)
        # 将numpy.ndarray转化成Tensor
        inputs = fluid.dygraph.to_variable(x_data)
        label = fluid.dygraph.to_variable(y_data)
        # 计算模型输出
        logits = model(inputs)
        # 计算损失函数
        loss = fluid.layers.softmax_with_cross_entropy(logits, label)  # 使用Cross Entropy交叉熵作为损失函数
        avg_loss = fluid.layers.mean(loss)  # 对求得的损失取平均值

        # print("epoch: {}, loss is: {}".format(epoch, avg_loss.numpy()))
    
        avg_loss.backward()
        opt.minimize(avg_loss)
        model.clear_gradients()

# 对模型进行评估的函数
def val(model, x_test, y_test):
    model.eval()
    accuracies = []
    
    # 调整输入数据形状和类型
    x_data = np.array(x_test, dtype='float32').reshape(-1, x_test.shape[1])
    y_data = np.array(y_test, dtype='int64').reshape(-1, 1)
    # 将numpy.ndarray转化成Tensor
    inputs = fluid.dygraph.to_variable(x_data)
    label = fluid.dygraph.to_variable(y_data)
    # 计算模型输出
    logits = model(inputs)
    pred = fluid.layers.softmax(logits)
    # 计算损失函数
    loss = fluid.layers.softmax_with_cross_entropy(logits, label)
    acc = fluid.layers.accuracy(pred, label)
    accuracies.append(acc.numpy())

    print("[validation] accuracy: {}".format(np.mean(accuracies)))

    return np.mean(accuracies)

def predict(model, x):
    model.eval()
    accuracies = []
    
    # 调整输入数据形状和类型
    x_data = np.array(x, dtype='float32').reshape(-1, x.shape[1])
    
    # 将numpy.ndarray转化成Tensor
    inputs = fluid.dygraph.to_variable(x_data)

    # 计算模型输出
    logits = model(inputs)
    pred = fluid.layers.softmax(logits)
    
    return pred


def getTrainingData():
    # 读入正样本
    positive = pd.read_csv('Data/positive_training_ld.csv')
    positive.drop(['学号'], axis=1, inplace=True)

    # 读入负样本
    negative = pd.read_csv('Data/NegativeTraining.csv')
    negative.drop(['学号'], axis=1, inplace=True)

    # 随机打乱负样本顺序
    negative = shuffle(negative)

    return positive, negative

def getTestingData():
    data = pd.read_csv('Data/testing_output_ld.csv')
    data.drop(['学号'], axis=1, inplace=True)
    return data

def main():
    # 从文件中读入训练集
    positive, negative = getTrainingData()
    
    # 从文件中读入测试集
    Testingdata = getTestingData()

    for i in range(5):
        # 获得需要的数据
        data = positive
        data = shuffle(data)

        # 得到X, y
        y = data['获奖类别']
        X = data.iloc[:, :-1]

        # 分割训练集与测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
        X_train.iloc[:, :-1], X_test.iloc[:, :-1] = scale(X_train.iloc[:, :-1]), scale(X_test.iloc[:, :-1])
        testing = scale(Testingdata.iloc[:, :-1])

        # 创建模型
        with fluid.dygraph.guard():
            # 我们将会发现，在训练过程中，随着迭代次数的增加，loss会逐渐降低，准确率会逐渐增高
            model = Model()
            train(model, X_train, y_train)
            accuracy = val(model, X_test, y_test)
            test = predict(model, testing)
            print(test)

               
        
        
if __name__ == "__main__":
    main()