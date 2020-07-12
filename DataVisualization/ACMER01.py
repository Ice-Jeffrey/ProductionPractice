# 用途：调用api，并绘制折线图显示某位同学cf积分的变化情况

import json
import time

import requests
import seaborn
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Line
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

# 获取某位同学cf积分的变化情况
def getCfRatings(sid):
    url = 'http://acmer.site/api/studentcontests/?format=json&type=1&stuNO=' + str(sid)
    html = getUrlText(url)
    js = json.loads(html)

    if len(js) < 1: 
        return

    x = []
    y = []
    for i in range(1, len(js)+1):
        x.append(str(i))
        y.append(js[i-1]['newRating'])
    
    # 绘制折线图
    line = Line(init_opts=opts.InitOpts(page_title='CF ratings of {}'.format(sid)))
    line.set_global_opts(
        title_opts=opts.TitleOpts(title='CF ratings of {}'.format(sid)),
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(
            type_="category", 
            name="ith CF contest",
            name_location='middle'
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name='CF Rating',
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    line.add_xaxis(xaxis_data=x)
    line.add_yaxis(
        series_name="CF Rating",
        y_axis=y,
        symbol="Circle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),
    )
    line.render("acmersite01_basic_line_chart.html")

def acmersite1():
    # sid = input()
    sid = '2017040266'
    getCfRatings(sid)

if __name__ == "__main__":
    acmersite1()