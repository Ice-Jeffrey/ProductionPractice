# 对buctoj中的重要信息进行爬取
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup # 需要用到beautifulsoup对网站进行解析
import requests
import json, time

# 获取html网页中信息的函数
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

def SubmitCrawler(StuNo, Language, Year, Result=None):
    # 爬取用户提交数与解决数
    url = 'http://39.106.31.26/status.php?'
    nextUrl = ''

    # 指定学生学号
    if StuNo:
        url += '&user_id=' + StuNo
    
    # 指定编程语言
    if Language:
        url += '&language=' + Language

    # 对提交状态进行筛选
    if Result != None:
        url += '&jresult=4'

    # 统计所有的提交记录数
    num = 0
    tempList = []   # 存放提交id的容器
    while True:
        # print(url)

        # 对提交的编程语言进行映射
        html = getUrlText(url)
        
        # 进行网址解析
        soup = BeautifulSoup(html, features='html.parser')

        # 进行css选择
        table = soup.select('tbody')

        # 对特殊情况进行判断
        if len(table) > 0:
            t = table[0]
        else:
            continue

        for index, tr in enumerate(t.select('tr')):
            result = tr.select('td')
            time = result[8].text[0:4]
            # 由于页面布局原因，可能不同的页面有相同的提交id，因此需要判断提交id是否存在，若不存在且满足条件，则进行抓取
            if time <= Year and result[0] not in tempList:
                num += 1
                tempList.append(result[0])

        # 获取下一页url
        nextUrl = soup.select('a')
        nextUrl = nextUrl[-1]['href']
        nextUrl = 'http://39.106.31.26/' + nextUrl

        if url == nextUrl:
            break
        else:
            url = nextUrl

    return num
        

# main函数
def main():
    DefaultData = pd.read_csv('F:\Codes\ProductionPractice\OutputData\ExcelData2.csv')

    # 初始化新的特征
    DefaultData['OJ提交数'], DefaultData['OJ正确数'], DefaultData['OJ准确率'] = 0, 0, 0

    falseList = []
    for index, item in enumerate(DefaultData.loc[:, ['学号', '年份', '科目名称']].values):
        Submit, AC = 0, 0
        print('爬取第', index, '条数据中......')
        # print(item[2], type(item[2]))

        if item[2] == 0:
            Submit = SubmitCrawler(str(item[0]), '0', str(item[1])) + SubmitCrawler(str(item[0]), '1', str(item[1]))
            AC = SubmitCrawler(str(item[0]), '0', str(item[1]), 'AC') + SubmitCrawler(str(item[0]), '1', str(item[1]), 'AC')

        if item[2] == 1:
            Submit = SubmitCrawler(str(item[0]), '3', str(item[1]))
            AC = SubmitCrawler(str(item[0]), '3', str(item[1]), 'AC')

        elif item[2] == 2:
            Submit = SubmitCrawler(str(item[0]), '6', str(item[1]))
            AC = SubmitCrawler(str(item[0]), '6', str(item[1]), 'AC')
    
        DefaultData.loc[index, 'OJ提交数'] = Submit
        DefaultData.loc[index, 'OJ正确数'] = AC

        if Submit != 0:
            DefaultData.loc[index, 'OJ准确率'] = AC / Submit
        else:
            # print(index)
            falseList.append(index)
    print('爬取结束')

    print(DefaultData)
    print(falseList)
    DefaultData.to_csv(
        'OutputData/ExcelData3.csv', 
        index=False, 
        columns = [
            '学号', '考生姓名', '科目名称', '性别', '专业', '年份', '编程年份', 
            '国家级一等奖', '国家级二等奖', '国家级三等奖', '国家级优秀奖',
            '省部级一等奖', '省部级二等奖', '省部级三等奖', '省部级优秀奖', 
            'OJ提交数', 'OJ正确数', 'OJ准确率',
            '获奖类别'
        ]
    )

# 默认的函数入口
if __name__ == "__main__":
    main()