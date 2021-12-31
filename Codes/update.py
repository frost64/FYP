
import nltk
nltk.download('stopwords')

# from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
from gensim.utils import tokenize

from nltk.corpus import stopwords
stopwords = [word for word in stopwords.words('english')]

import process

global processed

def updated_sentence(sentence): 
    sentence = sentence.lower()
    new = " "
    p = PorterStemmer()
    # print("before remove stopward : ",sentence)
    processed=process.pre_process(sentence)
    processed
    # print("processed : " ,processed)
    stemmed = p.stem(processed)
    # print(stemmed)
    tokens = tokenize(stemmed.strip())
    lst=list(tokens)
    lst2 = []
    for i in lst:
        #using nltk dic for stopwords
        if  i not in stopwords :
            lst2.append(i)
    return (new.join(lst2))
