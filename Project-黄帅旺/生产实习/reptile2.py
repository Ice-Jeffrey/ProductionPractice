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

def getStudentInfo(url):
    html = getUrlText(url)
    soup = BeautifulSoup(html,features='html.parser')
    table = soup.select('body')
    if len(table) > 0:
        t = table[0]
    else:
        return []
    data_list=[]
    tds=[]
    for idx,tr  in enumerate(t.select('tr')):
        if idx!=0:
            tds=tr.select('td')
            
    

if __name__=="__main__":
    url="http://39.106.31.26/userinfo.php?user=2018170037"
    getStudentInfo(url)