# !pip install textblob 
# !pip install scikit-learn
# !pip install gensim
# !pip install nltk
# !pip install seaborn
# !pip install textblob 
# !pip install skfeature-chappers

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
# %matplotlib inline

from textblob import TextBlob 
import numpy as np
import re
import nltk
nltk.download('stopwords')

# from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
from gensim.utils import tokenize

from nltk.corpus import stopwords
stopwords = [word for word in stopwords.words('english')]

from sklearn import model_selection
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def listing():

    url = "C:\Users\ASJID\Desktop\Project\all_brands_export.csv"
    db=pd.read_csv(url,sep = ';')
    # txt=db["review"][0].split('.')[0]
    # tokenize_sentence(txt)
    # db

    # reviews = np.array(da["review"])
    reviews = np.array(db["review"])
    myDict = {}
    list_ = []
    count = 0
    super_list = []
    for sent in reviews:

        temp= []
        try:
            temp = list(sent.split(","))
            super_list.append(temp)

        except:
            super_list.append(None)
    return super_list


def pre_process(sentence):  
# print(type(stopwords))


    # Remove all the special characters
    processed_sentence = re.sub(r'\W', ' ', str(sentence))

    # remove all single characters
    processed_sentence = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_sentence)

    # Remove single characters from the start
    processed_sentence= re.sub(r'\^[a-zA-Z]\s+', ' ', processed_sentence) 

    # Substituting multiple spaces with single space
    processed_sentence= re.sub(r'\s+', ' ', processed_sentence, flags=re.I)

    # Removing prefixed 'b'
    processed_sentence = re.sub(r'^b\s+', '', processed_sentence)
    
   
    return processed_sentence

def updated_sentence(sentence): 
    sentence = sentence.lower()
    new = " "
    p = PorterStemmer()
    # print("before remove stopward : ",sentence)
    processed = pre_process(sentence)
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

def polarity_scaling(polarity):
    # 0  nutral
    if polarity  == 0:
        return 0
    # greater then 0  positive
    elif polarity > 0:
        return 1
    else:
        # less then 0  negative
        return -1  

def reviews_list_polarity():
    individual_review = []
    for_reviews = []
    for_polarity = []
    super_list = listing()
    updated_review_Dict = {}
    super_list_2 = []
#     print(super_list)
    for remove_none_type in super_list:
        if remove_none_type is not None:
            super_list_2.append(remove_none_type)
#             print(super_list_2)
    for select_list in super_list_2:
        for i in select_list:
            news =i.strip()
            new1=news.split(".")

            lst_list = []
            lst_list_2 = []


            for j in new1:
                j = updated_sentence(j)
                temp =j.replace("\r\n" ,"")
                # print(temp)
                pol = TextBlob(temp).sentiment.polarity
                polarity=polarity_scaling(pol)
                tup = (temp ,polarity)
                lst_list.append(tup)
            # print(lst[0])
                # lst_list[:-1]
            for remove_tuple in lst_list:
                if remove_tuple != ('',0):
                    lst_list_2.append(remove_tuple)
#             print(lst_list_2[0][0])
            if lst_list_2 != []:
                for_reviews.append(lst_list_2[0][0])
                for_polarity.append(lst_list_2[0][1])
            
            # individual_review.append(lst_list_2)
    updated_review_Dict["reviews"]=for_reviews
    updated_review_Dict["polarity"]=for_polarity
    
           
            # print(lst_list)
            # individual_review.append(lst_list)

    # return updated_review_Dict["reviews"],updated_review_Dict["polarity"]
    return updated_review_Dict
    # return individual_review
# reviews_list_polarity()



def NB_training_testing():
    data=pd.DataFrame(reviews_list_polarity())
    #spiting data for train data
    x_train = data['reviews']
    y_train = data['polarity']
    x_train, x_test, y_train, y_test = train_test_split(x_train,y_train, stratify=y_train, test_size=0.25, random_state=42)
    
    # Vectorize text reviews to numbers
    vec = CountVectorizer()
    x_train = vec.fit_transform(x_train).toarray()
    x_test = vec.transform(x_test).toarray()
    # print(x_test)
    #train model
    NB_model = MultinomialNB()
    NB_model.fit(x_train, y_train)
    #prediction on test
    y_pred = NB_model.predict(x_test)
    # confusion matric and report and accurcy
    print("\n")
    NB_cf_matrix = confusion_matrix(y_test,y_pred)
    # cf_matrix
    print("Naive Bayes Matrix , accuracy and f1-score\n\n")
    print("NB confussion matrix : \n",NB_cf_matrix)

    print(classification_report(y_test,y_pred))
    print(accuracy_score(y_test,y_pred))
    print("\n")
    print("\n")
    # NB_model.score(x_test, y_test)
    #plot 
    
    ax = sns.heatmap(NB_cf_matrix, annot=True, cmap='Blues')

    ax.set_title('Naive Bayes Confusion Matrix\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['-1','0','1'])
    ax.yaxis.set_ticklabels(['-1','0','1'])

    ## Display the visualization of the Confusion Matrix.
    plt.show()
return NB_model






def SVM_training_testing():
    data=pd.DataFrame(reviews_list_polarity())
    #spiting data for train data
    x_train = data['reviews']
    y_train = data['polarity']
    x_train, x_test, y_train, y_test = train_test_split(x_train,y_train, stratify=y_train, test_size=0.25, random_state=42)
    
    # Vectorize text reviews to numbers
    vec = CountVectorizer()
    x_train = vec.fit_transform(x_train).toarray()
    x_test = vec.transform(x_test).toarray()
    # print(x_test)
    #train model
    svm_model = SVC(kernel='linear')       #kernal linear
    svm_model.fit(x_train, y_train)
    #prediction
    svm_pred = svm_model.predict(x_test)
    svm_cf_matrix = confusion_matrix(y_test,svm_pred)
    # svm_cf_matrix
    print("SVM confusion Matrix , accuracy and f1-score\n\n")
    print("SVM confusion Matrix : \n",svm_cf_matrix)

    print(classification_report(y_test,svm_pred))
    print(accuracy_score(y_test,svm_pred))
    
    # svm_model.score(x_test, y_test)
    
    ax = sns.heatmap(svm_cf_matrix, annot=True, cmap='Blues')

    ax.set_title('Svm Confusion Matrix\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['-1','0','1'])
    ax.yaxis.set_ticklabels(['-1','0','1'])

    ## Display the visualization of the Confusion Matrix.
    plt.show()
return svm_model
    
    










def main():
    reviews_list_polarity();
    listing();
    updated_sentence(sentence);
    pre_process(sentence);
    polarity_scaling(polarity);
    NB=NB_training_testing();
    SVM= SVM_training_testing();

    seed = 7
    kfold = model_selection.KFold(n_splits=10, shuffle =True, random_state = seed)

    estimators = []
    model1 = NB
    estimators.append(('svm', NB))
    model2 = SVM
    estimators.append(('cart', SVM))

    ensemble = VotingClassifier(estimators , voting = 'hard')
    results = model_selection.cross_val_score(ensemble, x, y, cv=kfold)
    print("Ensemble result",results.mean())


if __name__ == "__main__":
    main()








