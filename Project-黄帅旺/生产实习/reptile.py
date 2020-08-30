from bs4 import BeautifulSoup
import requests
import json, time
import lxml
import re
import pandas as pd
import os
import csv
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

def getStudentId(url):
    html =  getUrlText(url)
    soup = BeautifulSoup(html,'html.parser')
    table = soup.select('tbody')
    if len(table) > 0:
        t = table[0]
    else:
        return []
    data_list=[]
    tds=[]
    csv_1=pd.read_csv('./data/awarded.csv',sep=',',usecols=[0])
    awarded=[]
    for item_1 in csv_1.iloc[:,0]: 
        awarded.append(str(item_1))
    for idx,tr  in enumerate(t.select('tr')):
        tds = tr.select('td')
        studentId = tds[1].select('a')[0].text
        if str(studentId) in awarded:
            print("包含")
        else:
            data_list.append(studentId)
    return data_list

if __name__=="__main__":
    num  =  0
    i=0
    studentIdList=[]
    for num in range(0,4200,50):
        url = "http://39.106.31.26/ranklist.php?start="+str(num)+"&scope="
        dataList = getStudentId(url)
        for item in dataList:
            studentIdList.append(item)
    
    
    dict=pd.DataFrame({'学号':studentIdList})
    dict['考生姓名']=0
    dict['科目名称']=0
    dict['性别']=0
    dict['专业']=0
    dict['年份']=0
    dict['编程年份']=0
    dict['国家级一等奖']=0
    dict['国家级二等奖']=0
    dict['国家级三等奖']=0
    dict['国家级优秀奖']=0
    dict['省部级一等奖']=0
    dict['省部级二等奖']=0
    dict['省部级三等奖']=0
    dict['省部级优秀奖']=0
    dict['获奖类别']=0						    		    					
    dict.to_csv('./data/info.csv', sep=',', index=False)  