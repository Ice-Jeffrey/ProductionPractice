from bs4 import BeautifulSoup
import requests
import json, time
import os
import pandas as pd
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

def getGameInfoByStudentId(url):
    html = getUrlText(url)
    js=json.loads(html)
    if js:
        datalist=[]
        for d in js:
            gameId=d["id"]
            Ctime = csv['id']['time']
            if True:
                return newRating
            newRating=d["newRating"]
            stuNO=d["stuNO"]
            datalist.append({
                'stuNO':stuNO,
                'gameId':gameId,
                'newRating':newRating
            })
        return datalist
    else:
        print("数据不存在")  
# 根据比赛id获取比赛信息 
def getGameTime(gameIdNumber):
    csv = pd.read_csv("./data/game.csv",sep=',',usecols=[1,2]) 
    gameId=[]
    gameTime=[]
    for item in csv.iloc[:,0]:
        gameId.append(item)
    for item in csv.iloc[:,1]:
        gameTime.append(item)
    dic = dict(map(lambda x,y:[x,y],gameId,gameTime))
    if dic.get(gameIdNumber):
        return dic.get(gameIdNumber)
    else:
        return False

if __name__ == "__main__":
    # 获取学号和获奖年份字典
    positive_csv = pd.read_csv('./data/test_acmer.csv')
    # test = positive_csv.head(10)
    
    
    for index, item in enumerate(positive_csv.values):
        print(item[0])
        stuId = item[0]
        year=item[1]
        url = "http://acmer.site/api/studentcontests/?format=json&stuNO="+str(int(stuId))+"&type=1"
        html = getUrlText(url)
        # print(url)
        js=json.loads(html)
        datalist=[]
        for d in js:
            gameId=d["id"]
            gameTime = getGameTime(gameId)
            newRating=d["newRating"]
            # print(gameTime, newRating)
            if str(gameTime)[0:4] == str(positive_csv.loc[index, '年份']):
                positive_csv.loc[index, 'cfRating'] = newRating
                print(stuId,newRating)
                break
    print(positive_csv.loc[:, ['学号', '年份', 'cfRating']])
    positive_csv.to_csv('./data/outputdata_test_data.csv',index=False)
            
        
        
