import pandas as pd
import csv

def get_median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2
if __name__=="__main__":
    csv_submit=pd.read_csv('./data/ParticipateInfo.csv',sep=',',usecols=[15])
    csv_right=pd.read_csv('./data/ParticipateInfo.csv',sep=',',usecols=[16])
    csv_correct_rate=pd.read_csv('./data/ParticipateInfo.csv',sep=',',usecols=[17])

    submit=[]
    right=[]
    for item in csv_submit.iloc[:,0]:
        submit.append(int(item))
    for item in csv_right.iloc[:,0]:
        right.append(int(item))
    median_submit=get_median(submit)
    median_right=get_median(right)
    median_correct_rate=median_right/median_submit
    print(median_submit)
    print(median_right)
    print(median_correct_rate)
    