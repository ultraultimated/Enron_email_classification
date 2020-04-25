# Script for generating character based features

import pandas as pd
from string import punctuation


def extract_character_based_features(doc):

    nr_chars = 0
    nr_alphabet = 0
    nr_upper = 0
    nr_lower = 0
    nr_numerics = 0
    nr_spaces = 0
    nr_punctuation = 0

    for word in doc:
        for char in str(word):
            if char.isalpha():
                nr_alphabet += 1
            if char.isupper():
                nr_upper += 1
            if char.islower():
                nr_lower += 1
            if char.isnumeric():
                nr_numerics += 1
            if char.isspace():
                nr_spaces += 1
            if char in punctuation:
                nr_punctuation += 1
                
    doc=doc.replace(" ","")
    doc=doc.replace("\n","")
    nr_chars=len(doc)
        
    #return nr_chars,nr_alphabet,nr_upper,nr_lower,nr_numerics,nr_spaces,nr_punctuation

    return pd.Series({"nr_chars" : nr_chars,
                     "nr_alphabet": nr_alphabet,
                     "nr_upper": nr_upper,
                     "nr_lower":nr_lower,
                     "nr_numerics": nr_numerics,
                     "nr_spaces": nr_spaces,
                     "nr_punctuation": nr_punctuation})
