

import review_list
import pandas as pd
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def splitting():
    data=pd.DataFrame(review_list.reviews_list_polarity())
    #spiting data for train data
    x = data['reviews']
    y= data['polarity']
  
    # Vectorize text reviews to numbers
    vec = TfidfTransformer()
    matrix_X = vec.fit_transform(x)

    #x_test = vec.transform(x_test)
    
    return y,matrix_X
