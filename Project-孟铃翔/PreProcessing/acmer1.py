import numpy as np
import pandas as pd
import requests, json
import time

# 获取学生名单
def getStudents():
    # 从文件中读入json文件
    data = pd.read_json('OutputData/Acmers.json', encoding='utf-8')
    # print(data)
    return data

# 获取html网页中信息的函数
def getUrlText(url):
    count = 0
    while True:
        if count > 10:
            return None

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
        count += 1

    return html

def dropUserlessStudents(students):
    # 查看对应的接口是否有学生个人信息，若没有，则直接将该学生drop掉
    falseList = []
    for i in range(students.shape[0]):
        stuNo = students.loc[i, 'stuNo']
        # print(stuNo)
        domain = "http://acmer.site/api/student/" + str(stuNo)
     
        html = getUrlText(domain)    # 调用自定义函数获取网页中的文本
        if html == None:
            falseList.append(i)
    
    students.drop(index=falseList, inplace=True)

    return students


def main():
    students = getStudents()
    # print(students)
    students = dropUserlessStudents(students)

    print(students)
    students.to_csv('OutputData/Acmers.csv', index=False)

if __name__ == "__main__":
    main()