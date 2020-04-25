# Script for generating semantic features
#import extract_email_info
import nltk
import spacy
import en_core_web_lg
import pandas as pd
from collections import Counter
nlp = en_core_web_lg.load()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def extract_semantic_features(content):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(content)
    greeting_words_list = ["Dear", "To Whom It May Concern", "Hello", "Hi"]
    nr_greeting = 0
    for word in content.split(" "):
        if word in greeting_words_list:
            nr_greeting += 1

    sid = SentimentIntensityAnalyzer()
    nr_positive_word = 0
    nr_neg_word = 0
    nr_named_entity = 0
    nr_neutral_word=0
    words=content.split(" ")
    words=list(filter(None, words))
    freq=Counter(words)
    #words=[w for w in freq.keys() ]
    
    #for token in content.split(" "):
    for token in freq.keys():
        #print (token,"--------")
        if token!=None:
            if (sid.polarity_scores(str(token))['compound']) >= 0.05:
                nr_positive_word += freq[token]
            elif (sid.polarity_scores(str(token))['compound']) <= -0.05:
                nr_neg_word += freq[token]
            elif -0.05 < (sid.polarity_scores(str(token))['compound'])<0.05:
                nr_neutral_word+=freq[token]
        
   
    content=nlp(content)
    for token in content:
        if token.ent_type_!="":
            nr_named_entity+=1
            
    return pd.Series({"nr_positive_word": nr_positive_word,
                      "nr_neg_word": nr_neg_word,
                      "nr_neutral_word": nr_neutral_word,
                      "nr_named_entity": nr_named_entity,
                     "score_semantic": scores['compound'],
                      "nr_greeting": nr_greeting})
        


# def extract_semantic_features(content):
#     """
#     Extract semantic features, such as:
#     - overall sentiment score per email
#     - number of emoticons per email
#     - number of greeting per email
#     - number of positive words per email
#     - number of negative words per email
#     - number of named entities per email
#     """
#     content = nlp(content)
#     sid = SentimentIntensityAnalyzer()
#     scores = sid.polarity_scores(content)
#     greeting_words_list = ["Dear", "To Whom It May Concern", "Hello", "Hi"]
#     nr_greeting = 0
#     for word in content.split(" "):
#         if word in greeting_words_list:
#             nr_greeting += 1
    
#     sid = SentimentIntensityAnalyzer()
#     nr_positive_word = 0
#     nr_neg_word = 0
#     nr_named_entity = 0

#     for token in content.split(" "):
#         if (sid.polarity_scores(str(token))['compound']) >= 0.5:
#             nr_positive_word += 1
#         elif (sid.polarity_scores(str(token))['compound']) <= -0.5:
#             nr_neg_word += 1
#         if token.ent_type_ != "":
#             nr_named_entity += 1
    

#     return pd.Series({"nr_positive_word": nr_positive_word,
#                       "nr_neg_word": nr_neg_word,
#                       "nr_named_entity": nr_named_entity,
#                      "score_semantic": scores['compound'],
#                       "nr_greeting": nr_greeting})