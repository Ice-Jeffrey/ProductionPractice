
# 降维前后各个模型的预测率

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
def function():
    svm_before=0.39
    svm_after=0.40

    LogisticRegression_before=0.35
    LogisticRegression_after=0.34
    
    knn_before=0.28
    knn_after=0.34

    gdbt_before=0.45
    gdbt_after=0.43

    DecisionTree_before=0.39
    DecisionTree_after=0.40

    AdaBoost_before=0.39
    AdaBoost_after=0.33

    prediction_before=[]
    prediction_after=[]

    prediction_before.append(svm_before)
    prediction_before.append(LogisticRegression_before)
    prediction_before.append(knn_before)
    prediction_before.append(gdbt_before)
    prediction_before.append(DecisionTree_before)
    prediction_before.append(AdaBoost_before)
    
    prediction_after.append(svm_after)
    prediction_after.append(LogisticRegression_after)
    prediction_after.append(knn_after)
    prediction_after.append(gdbt_after)
    prediction_after.append(DecisionTree_after)
    prediction_after.append(AdaBoost_after)

    print(prediction_before)
    print(prediction_after)

    c = (
        Bar()
        .add_xaxis(
            [
                "svm",
                "LogisticRegression",
                "knn",
                "gdbt",
                "DecisionTree",
                "AdaBoost",
            ]
        )
        .add_yaxis("降维前", prediction_before)
        .add_yaxis("降维后", prediction_after)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="降维前后模型预测准确率对比", subtitle="。"),
        )
        .render("graphdata/prediction.html")
    )

if  __name__ == "__main__":
    function()