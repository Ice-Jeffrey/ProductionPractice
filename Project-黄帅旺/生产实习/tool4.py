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
def function():
    url="http://acmer.site/api/contests/?format=json"
    html = getUrlText(url)
    js=json.loads(html)
    if js:
        datalist=[]
        for d in js:
            gameid=d["id"]
            cid=d["cid"]
            cdate=d["cdate"]
            datalist.append({
                'gameid':gameid,
                'cid':cid,
                'cdate':cdate
            })
        return datalist
    else:
        print("数据不存在")
    
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
        return False

if __name__ == "__main__":
    gameinfo = pd.read_csv('data/gameinfo.csv')
    cdate=gameinfo.loc[gameinfo['cid'] == 1392]['cdate']
    print(cdate)

    time = getGameTime(1392)
    print(time)