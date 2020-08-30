
#不同获奖类别oj提交数，正确数，正确率

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

def function():
    positive_training = pd.read_csv('okdata/positive_training.csv')
    # print(positive_training)
    awarded_accuracy=[]
    awarded_submit=[]
    awarded_right=[]
    awarded_cfRating=[]
    for i in range(1,8):
        temp1=0
        temp2=0
        temp3=0
        temp4=0
        count=0
        for index,item in enumerate(positive_training.values):
            if(item[-1]==i):
                temp1=temp1+item[17]
                temp2=temp2+item[16]
                temp3=temp3+item[15]
                temp4=temp4+item[19]
                count=count+1
        accuracy=temp1/count
        submit=temp3/count
        right=temp2/count
        cfRating=temp4/count
        awarded_accuracy.append(accuracy*100)
        awarded_submit.append(submit)
        awarded_right.append(right)
        awarded_cfRating.append(cfRating)
    
    print(awarded_submit)
    print(awarded_right)
        
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
        .add_yaxis("oj_提交数", awarded_submit)
        .add_yaxis("oj_正确数", awarded_right)
        .add_yaxis("oj_正确率", awarded_accuracy)
        .add_yaxis("cfRating", awarded_cfRating)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="不同获奖类别的指标"),
        )
        .render("graphdata/different_awarded.html")
    )

if __name__=="__main__":
    function()