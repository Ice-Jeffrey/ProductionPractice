import pandas as pd
from sklearn import preprocessing

def function():
    csv =  pd.read_csv('nultural/positive_training_ld.csv')
    data_list=[]
    list_a=[]
    for index, item in enumerate(csv.values):
        list_a=[]
        for i in range(1,12):
            list_a.append(float(item[i]))
        list_a_scaled=preprocessing.scale(list_a)
        for i in range(0,11):
            csv.iloc[index,i+1]=list_a_scaled[i]
    csv.to_csv('nultural/positive_training_Id_guiyihua.csv',index=False)

if __name__ == "__main__":
    function()
