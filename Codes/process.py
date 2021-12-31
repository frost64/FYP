
import re

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
