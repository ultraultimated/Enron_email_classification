# script for generating sentence based features
import pandas as pd
import statistics
import en_core_web_lg
import spacy
nlp = en_core_web_lg.load()
def extract_sentence_based_features(doc):
    '''
    Extract sentence based feature
    1) Number of sentences in an email
    2) Average number of words per sentence in an email
    3) Standard deviation of sentence length
    '''
    nr_sentences = 0
    avg_number_of_words_per_sent = 0
    std_deviation_len = 0
    words=doc.split(" ")
    words=list(filter(None, words))
    words=[w for w in words if w.isalpha() or w.endswith(".") or w.endswith(".") or w.endswith("!") or w.endswith("?")]
    nr_words=len(words)
    doc = nlp(doc)
    sentences = list(doc.sents)
    nr_sentences = len(sentences)
    word_std=[len(s) for s in sentences]
    
    avg_number_of_words_per_sent = nr_words / nr_sentences
    
    if len(word_std) > 1:
        std_deviation_len = statistics.stdev(word_std)
    else:
        # if there is only on one sentence in the email standard deviation will be 0
        std_devaiation_len = 0
    
    #return nr_sentences,avg_number_of_words_per_sent,std_deviation_len
    
    return pd.Series({"nr_sentences": nr_sentences,
                      "avg_number_of_words_per_sent": avg_number_of_words_per_sent,
                      "std_deviation_len": std_deviation_len}) 