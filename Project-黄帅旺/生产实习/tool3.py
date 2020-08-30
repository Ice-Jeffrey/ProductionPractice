from bs4 import BeautifulSoup
import requests
import json, time
import os
import pandas as pd
import csv
import random
import math

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

def function(positive_csv, y):
    test1 = positive_csv[(positive_csv[str(y)]!=0) ]
    mincfRating = test1.describe().loc['min',y]
    maxcfRating = test1.describe().loc['max',y]
    if mincfRating != None and maxcfRating != None:
        print(mincfRating,maxcfRating)
        print(random.randint(mincfRating,maxcfRating))
        test2 = positive_csv[(positive_csv[str(y)]==0) ]
        number=random.randint(mincfRating,maxcfRating)
        for index, item in enumerate(test2.values):
            # print(index)
            positive_csv.loc[test2.index[index], str(y)] = random.randint(mincfRating,maxcfRating)
    return positive_csv
    


if __name__ == "__main__":
    # positive_csv = pd.read_csv('./data/testing.csv')
    negative_data =  pd.read_csv('okdata/negative_data.csv')
    minN=0
    maxN=4
    for index,item in enumerate(negative_data.values):
        number = random.randint(minN,maxN)
        negative_data.loc[negative_data.index[index],'编程年份']=int(number)
    negative_data.to_csv('okdata/negative_outputdata.csv',index=False)


    
    