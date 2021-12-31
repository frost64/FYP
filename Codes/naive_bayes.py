
import seaborn as sns
import matplotlib.pyplot as plt
import split

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score




def NB_training_testing():
    
    y,matrix_X =split.splitting()
    #train model
    NB_model = MultinomialNB()
    NB_model.fit(matrix_X[:8000],y[:8000])
    #prediction on test
    y_pred=NB_model.predict(matrix_X[8000:])
    # confusion matric and report and accurcy
    print("\n")
    NB_cf_matrix = confusion_matrix(y[8000:],y_pred)
    # cf_matrix
    print("Naive Bayes Matrix , accuracy and f1-score\n\n")
    print("NB confussion matrix : \n",NB_cf_matrix)

    print(classification_report(y[8000:],y_pred))
    print(accuracy_score(y[8000:],y_pred))
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
