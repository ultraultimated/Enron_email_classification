# Script for generating syntactic based features
#import extract_email_info
import nltk
import spacy
import en_core_web_lg
import pandas as pd
nlp = en_core_web_lg.load()

def extract_syntactic_feature(doc):
    """
    1) Number of Part of Speech
    2) Number of Function Words per email
    3) Average length of noun/verbs
    """
    pos_list = []
    func_pos_list = ["PRON", "DET", "ADP", "CONJ", "AUX", "INTJ", "PART", "CCONJ", "PART"]
    nr_function = 0
    sum_length_np = 0
    avg_length_np = 0
    np_list = []
    doc = nlp(doc)
    for word in doc:
        pos_list.append(word.pos_)
    for pos in pos_list:
        if pos in func_pos_list:
            nr_function += 1
    for np in doc.noun_chunks:
        sum_length_np += len(np.text)
        np_list.append(np.text)
    if len(np_list) > 0:
        avg_length_np = sum_length_np/len(np_list)
        
    return pd.Series({"nr_pos": len(set(pos_list)), 
                      "nr_function": nr_function, 
                      "avg_length_np": avg_length_np})
        
    
    