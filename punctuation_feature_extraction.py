# Script for generating punctuation based features
import pandas as pd
def extract_punctuation_based_features(doc):

    nr_commas = 0
    nr_dots = 0
    nr_exclamation = 0
    nr_qmark = 0
    nr_colons = 0
    nr_semicolons = 0
    nr_hyphens = 0

    for word in doc:
        for char in str(word):
            if char == ',':
                nr_commas += 1
            if char == '.':
                nr_dots += 1
            if char == '!':
                nr_exclamation += 1
            if char == '?':
                nr_qmark += 1
            if char == ':':
                nr_colons += 1
            if char == ';':
                nr_semicolons += 1
            if char == '-':
                nr_hyphens += 1
                
    return pd.Series({"nr_commas":nr_commas,
                     "nr_dots":nr_dots,
                     "nr_exclamation":nr_exclamation,
                     "nr_qmark":nr_qmark,
                     "nr_colons":nr_colons,
                     "nr_semicolons":nr_semicolons,
                     "nr_hyphens":nr_hyphens})

