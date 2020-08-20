import numpy as np
import pandas as pd

# 获取学生名单
def getStudents():
    # 从文件中读入json文件
    data = pd.read_json('F:/Codes/ProductionPractice/OutputData/Acmers.json', encoding='utf-8')
    # print(data)
    return data

def main():
    students = getStudents()
    print(students)

    students.to_csv('OutputData/Acmers.csv')

if __name__ == "__main__":
    main()