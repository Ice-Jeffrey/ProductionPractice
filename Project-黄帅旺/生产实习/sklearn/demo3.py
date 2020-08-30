
# 得奖奖项和cfRating，oj提交数，oj正确数，oj正确率的相关系数
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

def function():
    csv = pd.read_csv('data/positive_training.csv')
    prize_contury_2=[]
    prize_contury_3=[]
    prize_contury_good=[]
    prize_province_1=[]
    prize_province_2=[]
    prize_province_3=[]
    
    cfRating_contury_2=[]
    cfRating_contury_3=[]
    cfRating_contury_good=[]
    cfRating_province_1=[]
    cfRating_province_2=[]
    cfRating_province_3=[]


    oj_accuracy_contury_2=[]
    oj_accuracy_contury_3=[]
    oj_accuracy_contury_good=[]
    oj_accuracy_province_1=[]
    oj_accuracy_province_2=[]
    oj_accuracy_province_3=[]
    
    oj_submit_contury_2=[]
    oj_submit_contury_3=[]
    oj_submit_contury_good=[]
    oj_submit_province_1=[]
    oj_submit_province_2=[]
    oj_submit_province_3=[]
    
    oj_right_contury_2=[]
    oj_right_contury_3=[]
    oj_right_contury_good=[]
    
    oj_right_province_1=[]
    oj_right_province_2=[]
    oj_right_province_3=[]

    for index,item in enumerate(csv.values):
        if item[8]!=0:
            prize_contury_2.append(item[8])
            cfRating_contury_2.append(int(item[19]))
            oj_accuracy_contury_2.append(float(item[17]))
            oj_right_contury_2.append(int(item[16]))
            oj_submit_contury_2.append(int(item[15]))
        if item[9]!=0:
            prize_contury_3.append(item[9])
            cfRating_contury_3.append(int(item[19]))
            oj_accuracy_contury_3.append(float(item[17]))
            oj_right_contury_3.append(int(item[16]))
            oj_submit_contury_3.append(int(item[15]))
        if item[10]!=0:
            prize_contury_good.append(item[10])
            cfRating_contury_good.append(int(item[19]))
            oj_accuracy_contury_good.append(float(item[17]))
            oj_right_contury_good.append(int(item[16]))
            oj_submit_contury_good.append(int(item[15]))
            
        if item[11]!=0:
            prize_province_1.append(item[11])
            cfRating_province_1.append(int(item[19]))
            oj_accuracy_province_1.append(float(item[17]))
            oj_right_province_1.append(int(item[16]))
            oj_submit_province_1.append(int(item[15]))
        if item[12]!=0:
            prize_province_2.append(item[12])
            cfRating_province_2.append(int(item[19]))
            oj_accuracy_province_2.append(float(item[17]))
            oj_right_province_2.append(int(item[16]))
            oj_submit_province_2.append(int(item[15]))
        if item[13]!=0:
            prize_province_3.append(item[13])
            cfRating_province_3.append(int(item[19]))
            oj_accuracy_province_3.append(float(item[17]))
            oj_right_province_3.append(int(item[16]))
            oj_submit_province_3.append(int(item[15]))
        
        
    prize_contury_2=pd.Series(prize_contury_2)
    prize_contury_3=pd.Series(prize_contury_3)
    prize_contury_good=pd.Series(prize_contury_good)
    prize_province_1=pd.Series(prize_province_1)
    prize_province_2=pd.Series(prize_province_2)
    prize_province_3=pd.Series(prize_province_3)
    

    cfRating_contury_2=pd.Series(cfRating_contury_2)
    cfRating_contury_3=pd.Series(cfRating_contury_3)
    cfRating_contury_good=pd.Series(cfRating_contury_good)
    
    cfRating_province_1=pd.Series(cfRating_province_1)
    cfRating_province_2=pd.Series(cfRating_province_2)
    cfRating_province_3=pd.Series(cfRating_province_3)
    
    
    oj_accuracy_contury_2=pd.Series(oj_accuracy_contury_2)
    oj_accuracy_contury_3=pd.Series(oj_accuracy_contury_3)
    oj_accuracy_contury_good=pd.Series(oj_accuracy_contury_good)

    oj_accuracy_province_1=pd.Series(oj_accuracy_province_1)
    oj_accuracy_province_2=pd.Series(oj_accuracy_province_2)
    oj_accuracy_province_3=pd.Series(oj_accuracy_province_3)
    
    
    oj_submit_contury_2=pd.Series(oj_submit_contury_2)
    oj_submit_contury_3=pd.Series(oj_submit_contury_3)
    oj_submit_contury_good=pd.Series(oj_submit_contury_good)
    
    oj_submit_province_1=pd.Series(oj_submit_province_1)
    oj_submit_province_2=pd.Series(oj_submit_province_2)
    oj_submit_province_3=pd.Series(oj_submit_province_3)
    
    
    oj_right_contury_2=pd.Series(oj_right_contury_2)
    oj_right_contury_3=pd.Series(oj_right_contury_3)
    oj_right_contury_good=pd.Series(oj_right_contury_good)
    
    oj_right_province_1=pd.Series(oj_right_province_1)
    oj_right_province_2=pd.Series(oj_right_province_2)
    oj_right_province_3=pd.Series(oj_right_province_3)
    
    corr_gust_accuracy_contury_2=0
    corr_gust_accuracy_contury_3=0
    corr_gust_accuracy_contury_good=0
    corr_gust_accuracy_province_1=0
    corr_gust_accuracy_province_2=0
    corr_gust_accuracy_province_3=0
    
    corr_gust_submit_contury_2=0
    corr_gust_submit_contury_3=0
    corr_gust_submit_contury_good=0
    corr_gust_submit_province_1=0
    corr_gust_submit_province_2=0
    corr_gust_submit_province_3=0

    corr_gust_cfRating_contury_2=0
    corr_gust_cfRating_contury_3=0
    corr_gust_cfRating_contury_good=0
    corr_gust_cfRating_province_1=0
    corr_gust_cfRating_province_2=0
    corr_gust_cfRating_province_3=0

    corr_gust_right_contury_2=0
    corr_gust_right_contury_3=0
    corr_gust_right_contury_good=0
    corr_gust_right_province_1=0
    corr_gust_right_province_2=0
    corr_gust_right_province_3=0

    corr_gust_accuracy_contury_2=round(prize_contury_2.corr(oj_accuracy_contury_2),4)
    corr_gust_accuracy_contury_3=round(prize_contury_3.corr(oj_accuracy_contury_3),4)
    corr_gust_accuracy_contury_good=round(prize_contury_good.corr(oj_accuracy_contury_good),4)
    
    corr_gust_accuracy_province_1=round(prize_province_1.corr(oj_accuracy_province_1),4)
    corr_gust_accuracy_province_2=round(prize_province_2.corr(oj_accuracy_province_2),4)
    corr_gust_accuracy_province_3=round(prize_province_3.corr(oj_accuracy_province_3),4)
    
    
    corr_gust_cfRating_contury_2=round(prize_contury_2.corr(cfRating_contury_2),4)
    corr_gust_cfRating_contury_3=round(prize_contury_3.corr(cfRating_contury_3),4)
    corr_gust_cfRating_contury_good=round(prize_contury_good.corr(cfRating_contury_good),4)

    corr_gust_cfRating_province_1=round(prize_province_1.corr(cfRating_province_1),4)
    corr_gust_cfRating_province_2=round(prize_province_2.corr(cfRating_province_2),4)
    corr_gust_cfRating_province_3=round(prize_province_3.corr(cfRating_province_3),4)

    
    corr_gust_submit_contury_2=round(prize_contury_2.corr(oj_submit_contury_2),4)
    corr_gust_submit_contury_3=round(prize_contury_3.corr(oj_submit_contury_3),4)
    corr_gust_submit_contury_good=round(prize_contury_good.corr(oj_submit_contury_good),4)
    
    corr_gust_submit_province_1=round(prize_province_1.corr(oj_submit_province_1),4)
    corr_gust_submit_province_2=round(prize_province_2.corr(oj_submit_province_2),4)
    corr_gust_submit_province_3=round(prize_province_3.corr(oj_submit_province_3),4)

    
    corr_gust_right_contury_2=round(prize_contury_2.corr(oj_right_contury_2),4)
    corr_gust_right_contury_3=round(prize_contury_3.corr(oj_right_contury_3),4)
    corr_gust_right_contury_good=round(prize_contury_good.corr(oj_right_contury_good),4)

    corr_gust_right_province_1=round(prize_province_1.corr(oj_right_province_1),4)
    corr_gust_right_province_2=round(prize_province_2.corr(oj_right_province_2),4)
    corr_gust_right_province_3=round(prize_province_3.corr(oj_right_province_3),4)
    
    corr_gust_accuracy=[]
    corr_gust_submit=[]
    corr_gust_right=[]
    corr_gust_cfRating=[]
    
    
    corr_gust_accuracy.append(corr_gust_accuracy_contury_2)
    corr_gust_accuracy.append(corr_gust_accuracy_contury_3)
    corr_gust_accuracy.append(corr_gust_accuracy_contury_good)
    
    corr_gust_accuracy.append(corr_gust_accuracy_province_1)
    corr_gust_accuracy.append(corr_gust_accuracy_province_2)
    corr_gust_accuracy.append(corr_gust_accuracy_province_3)

    
    corr_gust_submit.append(corr_gust_submit_contury_2)
    corr_gust_submit.append(corr_gust_submit_contury_3)
    corr_gust_submit.append(corr_gust_submit_contury_good)
    
    corr_gust_submit.append(corr_gust_submit_province_1)
    corr_gust_submit.append(corr_gust_submit_province_2)
    corr_gust_submit.append(corr_gust_submit_province_3)

    
    corr_gust_right.append(corr_gust_right_contury_2)
    corr_gust_right.append(corr_gust_right_contury_3)
    corr_gust_right.append(corr_gust_right_contury_good)
    
    corr_gust_right.append(corr_gust_right_province_1)
    corr_gust_right.append(corr_gust_right_province_2)
    corr_gust_right.append(corr_gust_right_province_3)

    
    corr_gust_cfRating.append(corr_gust_cfRating_contury_2)
    corr_gust_cfRating.append(corr_gust_cfRating_contury_3)
    corr_gust_cfRating.append(corr_gust_cfRating_contury_good)
    corr_gust_cfRating.append(corr_gust_cfRating_province_1)
    corr_gust_cfRating.append(corr_gust_cfRating_province_2)
    corr_gust_cfRating.append(corr_gust_cfRating_province_3)
    print(corr_gust_cfRating_province_3)
    
    c = (
        Bar()
        .add_xaxis(
            [
                "国2",
                "国3",
                "国优秀",
                "省1",
                "省2",
                "省3",
            ]
        )
        .add_yaxis("cfRating", corr_gust_cfRating)
        .add_yaxis("提交数", corr_gust_submit)
        .add_yaxis("正确数", corr_gust_right)
        .add_yaxis("正确率", corr_gust_accuracy)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="未定", subtitle="未定"),
        )
        # .render("graphdata/correlation_coefficient_id.html")
    )

if __name__=="__main__":
    function()