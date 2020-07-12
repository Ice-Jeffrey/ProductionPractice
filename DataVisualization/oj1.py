# 用途：从oj爬取排名前50的用户的准确率，绘制小提琴图，并根据年级进行区分绘制准确率盒图

import json
import time

import requests
import seaborn
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Boxplot
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

# 绘制小提琴图的函数
def paintVioliin(data, title):
    seaborn.violinplot(data)
    plt.title(title)
    plt.show()

# 绘制盒图
def paintBoxPlot(datadict, xtitle, ytitle, title):
    graph = Boxplot(init_opts=opts.InitOpts(page_title=title))
    graph.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        yaxis_opts=opts.AxisOpts(name='Accuracy')
    )

    graph.add_xaxis([xtitle])
    for key, value in sorted(datadict.items()):
        # 为了画图的标准性，小于5人的年级图片将不会被加入盒图
        if len(value) > 4:
            graph.add_yaxis(key, graph.prepare_data([value]))
    
    graph.render('buctoj2_boxplot.html')

# 爬取排名前50的用户
def getTop50UsersAccuracy():
    # 获取html网页
    url = 'http://39.106.31.26/ranklist.php'
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

        # 获取排名数据
        ranking = result[0].text
        # 获取id
        id = result[1].select('a')[0].text
        # 获取用户名
        username = result[2].select('div')[0].text
        # 解题数
        solved = result[3].select('a')[0].text
        # 提交数
        submit = result[4].select('a')[0].text

        datalist.append({
            'ranking': int(ranking),
            'id': id,
            'username': username,
            'solved': solved,
            'submit': submit,
            'ACC': int(solved) / int(submit)
        })
    
    # print('finished')
    return datalist

def buctoj1():
    # 爬取排名前50的用户
    tempList = getTop50UsersAccuracy()

    # 将所有用户的准确率放入一列表中
    AccuracyList = []
    for item in tempList:
        AccuracyList.append(float(item['ACC']))
    # print(AccuracyList)

    # 绘制小提琴图
    # seaborn.violinplot(AccuracyList)
    # plt.title('Accuracy Violin Graph of Top50 Users')
    # plt.show()

    # 调用函数进行绘制
    paintVioliin(data=AccuracyList, title="Accuracy Violin Graph of BUCTOJ's Top50 Users")

    # 根据排名前50同学的年级和准确率进行统计
    s = set()
    accuracyDict = {}
    for item in tempList:
        grade = item['id'][0:4]
        if grade.isdigit():
            s.add(grade)
            temp = accuracyDict.get(grade, [])
            if temp == []:
                accuracyDict[grade] = [item['ACC']]
            else:
                accuracyDict[grade].append(item['ACC'])
    # print(s, accuracyDict)

    # 调用函数绘制盒图
    paintBoxPlot(datadict=accuracyDict, xtitle='Grades', ytitle='Accuracy', title="BUCTOJ Top50 Users' Accuracy BoxPlot")

if __name__=="__main__":
    buctoj1()
