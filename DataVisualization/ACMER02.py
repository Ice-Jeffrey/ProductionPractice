# 用途：调用api，绘制柱状图表示个年月比赛数量统计

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
        contestInfo[item['cdate']][item['ctype']] = contestInfo[item['cdate']].get(item['ctype'], 0) + 1
    
    print(contestInfo)
    return contestInfo

def paintBar():
    pass

def acmersite02():
    ContestInfo = getContestInfo()
    

if __name__ == "__main__":
    acmersite02()