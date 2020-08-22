import numpy as np
import pandas as pd
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

# 获取学生名单
def getStudents(school=1):
    # 根据api字段设置domain，注意domian前加http://，否则得不到正确连接
    domain = "http://acmer.site/api/students/?format=json" + '&school=' + str(school)
     
    html = getUrlText(domain)    # 调用自定义函数获取网页中的文本
    js = json.loads(html)    # 将html用json格式打开

    # 爬取数据
    datalist = []
    for item in js:
        datalist.append({
            'stuNo': item['stuNO'],
            # 'realName': item['realName'],
            # 'className': item['className'],
            # 'sex': item['sex'],
            'year': item['year'],
            'acRating': item['acRating'],
            'cfRating': item['cfRating'],
            'ncRating': item['ncRating'],
            'jskRating': item['jskRating'],
            'acTimes': item['acTimes'],
            'cfTimes': item['cfTimes'],
            'ncTimes': item['ncTimes'],
            'jskTimes': item['jskTimes'],
            'all_cf_aftersolve': item['all_cf_aftersolve'],
            'correct_cf_aftersolve': item['correct_cf_aftersolve'],
            'all_ac_aftersolve': item['all_ac_aftersolve'],
            'correct_ac_aftersolve': item['correct_ac_aftersolve']
        })

    return datalist

def main():
    students = getStudents()

    # print(students)
    # 写入 JSON 数据
    with open('OutputData/Acmers.json', 'w') as f:
        json.dump(students, f)

if __name__ == "__main__":
    main()