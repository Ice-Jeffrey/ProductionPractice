import pandas as pd

def LowerTheDimension(filename):
    data = pd.read_csv(filename)

    data['省部级获奖数'] = data['省部级一等奖'] + data['省部级二等奖'] + data['省部级三等奖'] + data['省部级优秀奖']
    data['国家级获奖数'] = data['国家级一等奖'] + data['国家级二等奖'] + data['国家级三等奖'] + data['国家级优秀奖']

    data.drop(['国家级一等奖', '国家级二等奖', '国家级三等奖', '国家级优秀奖', 
        '省部级一等奖', '省部级二等奖', '省部级三等奖', '省部级优秀奖'], axis=1, inplace=True)
    print(data)
    return data


def main():
    paths = ['Data/positive_training.csv', 'Data/negative_training.csv', 'Data/testing_output.csv']
    for _file in paths:
        data = LowerTheDimension(_file)
        data.to_csv(_file[:-4] + '_ld.csv', index=False)

if __name__ == "__main__":
    main()