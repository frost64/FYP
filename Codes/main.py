import listing
import naive_bayes
from sklearn.ensemle import VotingClassifier
from sklearn import model_selection
import svm
import split
import review_list




def main():
    
    
    
    

    review_list.reviews_list_polarity();
    listing.listing();
    NB_model=naive_bayes.NB_training_testing();
    svm_model=svm.SVM_training_testing()
    
    
    
    
    models = [('NB',NB_model),('svm',svm_model)]
    ensemble = VotingClassifier(estimators=models)
    results=model_selection.cross_val_score(ensemble, split.matrix_X[:8000], split.sy[:8000])
    print("Ensembler Majority voting ",results.mean(),results)


if __name__ == "__main__":
    main()
