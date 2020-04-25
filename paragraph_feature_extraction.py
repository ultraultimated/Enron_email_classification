# Script for generating paragraph based features

import pandas as pd
import re
from collections import Counter
import en_core_web_lg
import spacy
nlp = en_core_web_lg.load()
def extract_paragraph_based_features(doc):

    num_paras = 0
    av_sent = 0
    av_words = 0
    num_sents = 0
    num_words = 0

    paragraphs = doc.split("\n\n")
    paragraphs = [paragraph for paragraph in paragraphs if not (paragraph.isspace() or paragraph == "")]
    num_paras = len(paragraphs)
    doc=str(doc)
    freq=Counter(doc.split())
    words=[freq[w] for w in freq.keys() ]#if w.isalpha() or w.endswith(".") or w.endswith("!") or w.endswith("?") or w.endswith(",")]
    #print (sum(words))
    num_words=sum(words)
    
    
    doc = nlp(doc)
    sentences = list(doc.sents)
    num_sents = len(sentences)
    
    av_sent = num_sents / num_paras
    av_words = num_words / num_paras
    
    return pd.Series({"num_paras": num_paras, 
                      "av_sent": av_sent, 
                      "av_words": av_words})

