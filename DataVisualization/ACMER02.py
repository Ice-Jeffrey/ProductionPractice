# 用途：调用api，绘制柱状图表示各年月比赛数量统计

import json
import time

import requests
import seaborn
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 自定义函数显示html网页文本
def getUrlText(url):
    while True:
        try:
            html = requests.get(url)
            html = html.text
            break
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(3)    
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
            time.sleep(3)
    return html

# 获取比赛的详细信息
def getContestInfo():
    url = 'http://acmer.site/api/contests/?format=json'
    html = getUrlText(url)
    js = json.loads(html)

    if len(js) < 1:
        return {}
    
    datalist = []
    for i in range(len(js)):
        # 只需选取比赛的类型和年月即可
        datalist.append({
            'ctype': js[i]['ctype'],
            'cdate': js[i]['cdate'][:7] # 只需将日期精确到月即可
        })
    
    contestInfo = {}
    for item in datalist:
        flag = contestInfo.get(item['cdate'], None)
        if flag == None:
            contestInfo[item['cdate']] = {}
            contestInfo[item['cdate']]['total'] = 0 
        contestInfo[item['cdate']][item['ctype']] = contestInfo[item['cdate']].get(item['ctype'], 0) + 1
        contestInfo[item['cdate']]['total'] += 1
    
    # 返回对应年月不同比赛的数量
    # print(contestInfo)
    return contestInfo

# 自定义的画柱状图的函数
def paintGraph(contestInfo, starttime='2017-09', endtime='2020-07'):
    # 先根据指定的起始日期和截止日期构造需要的数据
    x, cf, ac, nc, jsk, total = [], [], [], [], [], []
    for key, value in sorted(contestInfo.items()):
        if key >= starttime and key <= endtime:
            x.append(key)
            cf.append({'value': value.get('cf', 0)})
            ac.append({'value': value.get('ac', 0)})
            nc.append({'value': value.get('nc', 0)})
            jsk.append({'value': value.get('jsk', 0)})
            total.append(value.get('total', 0))

    # print(total)

    # 绘制图表
    bar = Bar(
        init_opts=opts.InitOpts(
            theme=ThemeType.LIGHT, 
            page_title='各年月比赛数量统计'
        )
    )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title='各年月比赛数量统计'),
        xaxis_opts=opts.AxisOpts(name='比赛年月'),
        yaxis_opts=opts.AxisOpts(name='比赛数量统计')
    )
    bar.add_xaxis(x)
    bar.add_yaxis("CodeForces", cf, stack="stack1", category_gap="50%")
    bar.add_yaxis("NowCoder", nc, stack="stack1", category_gap="50%")
    bar.add_yaxis("AtCoder", ac, stack="stack1", category_gap="50%")
    bar.add_yaxis("计蒜客", jsk, stack="stack1", category_gap="50%")
    bar.set_series_opts(
        label_opts=opts.LabelOpts(
            position="inside",
            formatter=JsCode(
                "function(x){return x.data.value ? Number(x.data.value) : '';}"
            ),
        )
    )

    line = Line()
    line.set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    line.add_xaxis(xaxis_data=x)
    line.add_yaxis(
        series_name="total",
        y_axis=total,
        symbol="Circle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),
    )

    # 将柱状图与折线图一起输出到html文件中
    bar.overlap(line).render('acmersite02.html')


def acmersite02():
    ContestInfo = getContestInfo()
    # startime = input("请输入起始时间：")
    # endtime = input("请输入截止时间：")
    startime = '2017-09'
    endtime = '2020-07'
    paintGraph(contestInfo=ContestInfo, starttime=startime, endtime=endtime)
    

if __name__ == "__main__":
    acmersite02()