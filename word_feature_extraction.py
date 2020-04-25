# Script for word based features
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import en_core_web_lg
nlp = en_core_web_lg.load()
from collections import Counter
from operator import itemgetter
vocab_list = list(nlp.vocab.strings)
stop_words = set(stopwords.words('english'))
def extract_word_based_features(doc):
    """
    Extract word based features, such as:
    - number of words per email
    - avrage number of characters per word in the email
    - number of longwords(more than 5 letters) per email
    - number of stopwords per email
    - number of spelling error per email
    - The TTR (type-token ratio) in the email
    - The HTR (hapax legomena/token ratio) in the email
    - frequency of most-frequent words in the email
    """

    long_word = 5
    nr_words = 0
    sum_characters = 0
    avg_characters_per_word = 0
    nr_longwords = 0
    nr_stopwords = 0
    nr_error = 0

    freq=Counter(doc.split())
    words=[freq[w] for w in freq.keys() ]#if w.isalpha() or w.endswith(".") or w.endswith("!") or w.endswith("?") or w.endswith(",")]
    #print (sum(words))
    nr_words=sum(words)
    
    char_doc=doc.replace(" ","")
    char_doc=doc.replace("\n","")
    nr_chars=len(char_doc)
    
    for token in doc.split(" "):
        if token.isalpha():
            if len(token) > long_word:
                nr_longwords += 1
            if token in stop_words:
                nr_stopwords += 1
            if not token in vocab_list:
                nr_error += 1
    if nr_words > 0:
        avg_characters_per_word = nr_chars / nr_words
    else:
        avg_characters_per_word = 0

    return pd.Series({"nr_words": nr_words,
                      "avg_characters_per_word": avg_characters_per_word,
                      "nr_longwords": nr_longwords,
                      "nr_stopwords": nr_stopwords,
                      "nr_error": nr_error})

    