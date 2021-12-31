
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import split


def SVM_training_testing():
    y ,matrix_X= split.splitting()
    # print(x_test)
    #train model
    svm_model = SVC(kernel='linear')
    svm_model.fit(matrix_X[:8000],y[:8000])
    svm_pred=svm_model.predict(matrix_X[8000:])
    svm_cf_matrix = confusion_matrix(y[8000:],svm_pred)
    # svm_cf_matrix
    print("SVM confusion Matrix , accuracy and f1-score\n\n")
    print("SVM confusion Matrix : \n",svm_cf_matrix)

    print(classification_report(y[8000:],svm_pred))
    print(accuracy_score(y[8000:],svm_pred))
    
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
    
   