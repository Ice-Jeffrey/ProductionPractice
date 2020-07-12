# 用途：从oj爬取某次比赛各个题目的准确率，绘制柱状图

import json
import time

import requests
import seaborn
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Bar
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

# 爬取某次比赛各题目信息
def getContestAcc(cid):
    url = 'http://39.106.31.26/contest.php?cid=' + str(cid)
    html = getUrlText(url)

    # 进行网址解析
    soup = BeautifulSoup(html, features='html.parser')

    # 进行css选择
    table = soup.select('tbody')
    
    if len(table) > 0:
        t = table[0]
    else:
        return []

    datalist = []
    for index, tr in enumerate(t.select('tr')):
        result = tr.select('td')

        # 获取问题
        pid = result[1].text[-1]
        # 获取问题名字
        ptitle = result[2].select('a')[0].text
        # 正确提交数
        solved = result[4].text
        # 提交数
        submit = result[5].text

        datalist.append({
            'pid': pid,
            'ptitle': ptitle,
            'solved': solved,
            'submit': submit,
            'ACC': int(solved) / int(submit)
        })
    
    # print('finished')
    return datalist

# 绘制柱状图
def paintBar(datalist, cid):
    axis = []
    AC = []
    WA = []
    for item in datalist:
        axis.append(item['pid'] + '(' + item['ptitle'] + ')')
        AC.append({
            'value': int(item['solved']),
            'percent': item['ACC']
        })
        WA.append({
            'value': int(item['submit']) - int(item['solved']),
            'percent': (int(item['submit']) - int(item['solved'])) / int(item['submit'])
        })

    # print(axis, end='\n\n')
    # print(len(axis), len(AC), len(WA))
    # for item in AC:
    #     print(item)
    # print('\n')
    # print('\n')
    # for item in WA:
    #     print(item)

    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, page_title='Accuracy Bar of the Contest whose id is {}'.format(str(cid))))
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title='Accuracy Bar of the Contest whose id is {}'.format(str(cid))),
        yaxis_opts=opts.AxisOpts(name='Accuracy'),
        xaxis_opts=opts.AxisOpts(name='Problem Index', name_location='middle')
    )
    bar.add_xaxis([x+1 for x in range(len(axis))])
    bar.add_yaxis('AC', AC, stack='stack1', category_gap='50%')
    bar.add_yaxis('WA', WA, stack='stack1', category_gap='50%')
    bar.set_series_opts(
        label_opts=opts.LabelOpts(
            position='right',
            formatter=JsCode(
                "function(x) {return Number(x.data.percent*100).toFixed() + '%';}"
            )
        )
    )
    bar.render('buctoj3_stack_bar_percent.html')

def buctoj2():
    # cid = int(input())
    ProblemList = getContestAcc(cid=1802)
    paintBar(ProblemList, cid=1802)

if __name__ == "__main__":
    buctoj2()