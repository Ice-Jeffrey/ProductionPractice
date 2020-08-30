
# oj准确率和cfRating相关系数

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
import pylab as plt
from pyecharts import options as opts
from pyecharts.charts import Bar
def function():
    positive_training = pd.read_csv('okdata/positive_training.csv')
    
    awarded_1_cfRating=[]
    awarded_1_accuracy=[]

    awarded_2_cfRating=[]
    awarded_2_accuracy=[]

    awarded_3_cfRating=[]
    awarded_3_accuracy=[]

    awarded_4_cfRating=[]
    awarded_4_accuracy=[]

    awarded_5_cfRating=[]
    awarded_5_accuracy=[]

    awarded_6_cfRating=[]
    awarded_6_accuracy=[]

    awarded_7_cfRating=[]
    awarded_7_accuracy=[]
    for i in range(1,8):
        for index,item in enumerate(positive_training.values):
            if(item[-1]==1):
                awarded_1_cfRating.append(int(item[19]))
                awarded_1_accuracy.append(float(item[17]))
            if(item[-1]==2):    
                awarded_2_cfRating.append(int(item[19]))
                awarded_2_accuracy.append(float(item[17]))
            if(item[-1]==3):    
                awarded_3_cfRating.append(int(item[19]))
                awarded_3_accuracy.append(float(item[17]))
            if(item[-1]==4):    
                awarded_4_cfRating.append(int(item[19]))
                awarded_4_accuracy.append(float(item[17]))
            if(item[-1]==5):    
                awarded_5_cfRating.append(int(item[19]))
                awarded_5_accuracy.append(float(item[17]))
            if(item[-1]==6):    
                awarded_6_cfRating.append(int(item[19]))
                awarded_6_accuracy.append(float(item[17]))
            if(item[-1]==7):    
                awarded_7_cfRating.append(int(item[19]))
                awarded_7_accuracy.append(float(item[17]))

    awarded_1_accuracy=pd.Series(awarded_1_accuracy)
    awarded_1_cfRating=pd.Series(awarded_1_cfRating)

    awarded_2_accuracy=pd.Series(awarded_2_accuracy)
    awarded_2_cfRating=pd.Series(awarded_2_cfRating)

    awarded_3_accuracy=pd.Series(awarded_3_accuracy)
    awarded_3_cfRating=pd.Series(awarded_3_cfRating)

    awarded_4_accuracy=pd.Series(awarded_4_accuracy)
    awarded_4_cfRating=pd.Series(awarded_4_cfRating)

    awarded_5_accuracy=pd.Series(awarded_5_accuracy)
    awarded_5_cfRating=pd.Series(awarded_5_cfRating)

    awarded_6_accuracy=pd.Series(awarded_6_accuracy)
    awarded_6_cfRating=pd.Series(awarded_6_cfRating)

    awarded_7_accuracy=pd.Series(awarded_7_accuracy)
    awarded_7_cfRating=pd.Series(awarded_7_cfRating)

    corr_gust_1 = round(awarded_1_accuracy.corr(awarded_1_cfRating), 4)
    corr_gust_2 = round(awarded_2_accuracy.corr(awarded_2_cfRating), 4)
    corr_gust_3 = round(awarded_3_accuracy.corr(awarded_3_cfRating), 4)
    corr_gust_4 = round(awarded_4_accuracy.corr(awarded_4_cfRating), 4)
    corr_gust_5 = round(awarded_5_accuracy.corr(awarded_5_cfRating), 4)
    corr_gust_6 = round(awarded_6_accuracy.corr(awarded_6_cfRating), 4)
    corr_gust_7 = round(awarded_7_accuracy.corr(awarded_7_cfRating), 4)
    corr_gust=[]
    corr_gust.append(corr_gust_1)
    corr_gust.append(corr_gust_2)
    corr_gust.append(corr_gust_3)
    corr_gust.append(corr_gust_4)
    corr_gust.append(corr_gust_5)
    corr_gust.append(corr_gust_6)
    corr_gust.append(corr_gust_7)
    print(corr_gust)
    print(corr_gust_1)
    print(corr_gust_2)
    print(corr_gust_3)
    print(corr_gust_4)
    print(corr_gust_5)
    print(corr_gust_6)
    print(corr_gust_7)
    # plt.scatter(awarded_1_accuracy, awarded_1_cfRating)
    # plt.title('corr_gust :' + str(corr_gust_1), fontproperties='SimHei') #给图写上title
    # plt.show()
    c = (
        Bar()
        .add_xaxis(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
            ]
        )
        .add_yaxis("相关系数", corr_gust)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
        )
        .render("graphdata/Correlation_coefficient.html")
    )
if __name__=="__main__":
    function()