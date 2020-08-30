from pyecharts import options as opts
from pyecharts.charts import Bar

list_a=[0.42,0.45,0.46,0.41,0.48,0.43,0.43]
c = (
    Bar()
    .add_xaxis(
        [
            "AdaBoost",
            "决策树",
            "GDBT",
            "KNN",
            "逻辑回归",
            "SVM",
            "神经网络",
            
        ]
    )
    .add_yaxis("预测率", list_a)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="各个模型预测准确率"),
    )
    .render("graphdata/everyprediction.html")
)
