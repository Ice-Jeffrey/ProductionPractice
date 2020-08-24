import numpy as np
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import paddle.fluid as fluid
import paddle
from paddle.fluid.dygraph.nn import Linear

# 自定义神经网络模型
class Model(fluid.dygraph.Layer):
    # 先定义网络的结构
    def __init__(self, num_classes=8):
        super(Model, self).__init__()
        self.fc1 = Linear(input_dim=16, output_dim=128, act='sigmoid') # 输入层和隐藏层的连接，隐藏层使用Sigmoid作为激活函数
        self.fc2 = Linear(input_dim=128, output_dim=num_classes) # 隐藏层和输出层的连接，输出层不使用激活函数

    # 网络的前向计算过程
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x

# 定义训练神经网络的函数
def train(model, x_train, y_train):
    print('start training ... ')
    model.train()
    epoch_num = 50     # 定义训练50轮
    opt = fluid.optimizer.Momentum(learning_rate=0.01, momentum=0.9, parameter_list=model.parameters()) #定义优化器为Momentum，学习率为0.01

    def reader_train():   # paddle中生成batch的辅助函数。
        for x, y in zip(x_train, y_train):
            yield x, y


    for epoch in range(epoch_num):
        train_loader = paddle.batch(paddle.reader.shuffle(reader_train,  #把输入数据打乱，把每10个数据组成一个batch。
                                                          buf_size=100),
                                                          batch_size=4)  
        for batch_id, data in enumerate(train_loader()):
            # 调整输入数据形状和类型
            x_data = np.array([item[0] for item in data], dtype='float32').reshape(-1, 16)
            y_data = np.array([item[1] for item in data], dtype='int64').reshape(-1, 1)
            # 将numpy.ndarray转化成Tensor
            inputs = fluid.dygraph.to_variable(x_data)
            label = fluid.dygraph.to_variable(y_data)
            # 计算模型输出
            logits = model(inputs)
            # 计算损失函数
            loss = fluid.layers.softmax_with_cross_entropy(logits, label)  # 使用Cross Entropy交叉熵作为损失函数
            avg_loss = fluid.layers.mean(loss)  # 对求得的损失取平均值
            
            # 每训练10次查看一下模型效果
            # if batch_id % 10 == 0:
            #     print("epoch: {}, batch_id: {}, loss is: {}".format(epoch, batch_id, avg_loss.numpy()))
            avg_loss.backward()
            opt.minimize(avg_loss)
            model.clear_gradients()

# 对模型进行评估的函数
def val(model, x_test, y_test):
    def reader_test():
        for x, y in zip(x_test, y_test):
            yield x, y
    valid_loader = paddle.batch(paddle.reader.shuffle(reader_test,
                          buf_size=100),
                          batch_size=4)
    model.eval()
    accuracies = []
    for batch_id, data in enumerate(valid_loader()):
        # 调整输入数据形状和类型
        x_data = np.array([item[0] for item in data], dtype='float32').reshape(-1, 16)
        y_data = np.array([item[1] for item in data], dtype='int64').reshape(-1, 1)
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

    solvers = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']

    for solver in solvers:
        for i in range(iter):
            # 获得需要的数据
            data = pd.concat([positive, negative.iloc[i * 228: (i+1)*228, :]], axis=0)
            # data = positive
            data = shuffle(data)

            # 得到X, y
            y = data['获奖类别']
            X = data.iloc[:, :-1]
            # X = data.iloc[:, :12]
            # print(X, y)

            # 分割训练集与测试集
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

            # 进行标准化
            scaler = StandardScaler().fit(X_train)
            Standardized_X_train = scaler.transform(X_train)
            Standardized_X_test = scaler.transform(X_test)

            scaler = StandardScaler().fit(Testingdata.iloc[:, :-1])
            Standardized_Testing = scaler.transform(Testingdata.iloc[:, :-1])

            # 创建模型
            with fluid.dygraph.guard():
                # 我们将会发现，在训练过程中，随着迭代次数的增加，loss会逐渐降低，准确率会逐渐增高
                model = Model()
                train(model, Standardized_X_train, y_train)
                val(model, Standardized_X_test, y_test)

               
        
        
if __name__ == "__main__":
    main()