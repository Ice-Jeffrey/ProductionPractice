# 用途：调用api，绘制柱状图表示按照cf积分排序现役Top50同学中北化同学与其他学校各年级情况

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

# 获取学生排名的详细信息
def getRankingList():
    url = 'http://acmer.site/api/students/?format=json&size=50&isactive=1&order=1'
    html = getUrlText(url)
    js = json.loads(html)

    if len(js) < 1:
        return []
    
    datalist = []
    for index, value in enumerate(js):
        datalist.append({
            'ranking': index+1,
            'school': value['school']
        })

    # print(datalist)
    return datalist

# 绘制柱状图进行数据分析
def paintGraph(datalist):
    buct, ntu = [0 for i in range(5)], [0 for i in range(5)]
    for item in datalist:
        if item['ranking'] > 0 and item['ranking'] <= 10:
            if item['school'] == '北京化工大学':
                buct[0] += 1
            elif item['school'] == '南通大学':
                ntu[0] += 1
        elif item['ranking'] > 10 and item['ranking'] <= 20:
            if item['school'] == '北京化工大学':
                buct[1] += 1
            elif item['school'] == '南通大学':
                ntu[1] += 1
        elif item['ranking'] > 20 and item['ranking'] <= 30:
            if item['school'] == '北京化工大学':
                buct[2] += 1
            elif item['school'] == '南通大学':
                ntu[2] += 1
        elif item['ranking'] > 30 and item['ranking'] <= 40:
            if item['school'] == '北京化工大学':
                buct[3] += 1
            elif item['school'] == '南通大学':
                ntu[3] += 1
        elif item['ranking'] > 40 and item['ranking'] <= 50:
            if item['school'] == '北京化工大学':
                buct[4] += 1
            elif item['school'] == '南通大学':
                ntu[4] += 1
        
    bar = Bar(init_opts=opts.InitOpts(page_title='现役CF积分Top50队员学校分布情况'))
    bar.add_xaxis(['1~10', '10~20', '20~30', '30~40', '40~50'])
    bar.add_yaxis('北京化工大学', buct)
    bar.add_yaxis('南通大学', ntu)
    bar.set_global_opts(title_opts=opts.TitleOpts(title='现役CF积分Top50队员学校分布情况'))
    bar.render('acmersite03.html')

# 入口函数 
def acmersite3():
    RankingList = getRankingList()
    paintGraph(RankingList)

if __name__ == "__main__":
    acmersite3()