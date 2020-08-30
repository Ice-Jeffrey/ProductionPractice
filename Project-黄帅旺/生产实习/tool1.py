import pandas as pd
import csv
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
def getGameTime(gameIdNumber):
    csv = pd.read_csv("./data/gameinfo.csv",sep=',',usecols=[1,2]) 
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
        return -1

def function():
    negative_training_csv = pd.read_csv('data/test2.csv')
    gameinfo_csv = pd.read_csv("data/gameinfo.csv")
    id_list=[]
    for index, item in enumerate(negative_training_csv.values):
        stuId=int(item[0])
        url="http://acmer.site/api/studentcontests/?stuNO="+str(stuId)+"&type=1"
        html = getUrlText(url)
        js=json.loads(html)
        id_list.append(int(item[0]))
        if js:
            datalist=[]
            for d in js:
                gameId=d["id"]
                stuNO=d["stuNO"]
                gameTime = getGameTime(gameId)
                gameTime = str(gameTime)[0:4]
                print(int(item[0]),gameTime)
                if int(gameTime)!=-1:
                    print(int(gameTime)-int(str(item[0])[0:4]))
                    year = int(gameTime)-int(str(item[0])[0:4])
                    negative_training_csv.loc[index, '编程年份'] = year
                datalist.append({
                    'stuNO':stuNO,
                    'gameId':gameId
                })
            #print(datalist)
        else:
            print("数据不存在")
    negative_training_csv.to_csv('okdata/test2data.csv',index=False)
if __name__ == "__main__":
    function()

    