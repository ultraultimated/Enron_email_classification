# Script for TTR and HTR features
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import en_core_web_lg
nlp = en_core_web_lg.load()
from collections import Counter
from operator import itemgetter

def extract_word_based_features(doc):
    doc=nlp(doc)
    TTR = 0
    hapaxes = []
    HTR = 0
    token_list = []
    sorted_token_frequency = []
    most_frequency = 0
    for token in doc:
        if str(token).isalpha():
            token_list.append(str(token))
            
    if len(token_list) > 0:
        TTR = len(set(token_list))/len(token_list)
        hapaxes = list(filter(lambda x: token_list.count(x) == 1, token_list))
        HTR = len(hapaxes)/len(token_list)
        sorted_token_frequency = sorted(Counter(token_list).items(), key=itemgetter(1), reverse=True)
        most_frequency = sorted_token_frequency[0][1]
    else:
        TTR = 0
        HTR = 0
        most_frequency = 0
    return pd.Series({ "TTR": TTR,
                      "HTR": HTR,
                      "most_frequency": most_frequency})