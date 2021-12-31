import pandas as pd
import numpy as np


def listing():

    url = "C:/Users/ASJID/Desktop/Project1/Project/all_brands_export.csv"
    db=pd.read_csv(url,sep= ';')

    reviews = np.array(db["review"])

    super_list = []
    for sent in reviews:

        temp= []
        try:
            temp = list(sent.split(","))
            super_list.append(temp)

        except:
            super_list.append(None)
    return super_list
