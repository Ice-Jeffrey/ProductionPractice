import numpy as np
import pandas as pd

def WritePredictions(filename, accuracyList, testList):
    data = pd.DataFrame()
    data['accuracy'] = accuracyList
    data['predictions'] = testList

    data.to_csv(filename, index=False)