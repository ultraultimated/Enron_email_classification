# Script for removing forwarded chains

import pandas as pd
import re


def new_content(row):
    lines=row.splitlines()
    #print (lines)
    final=[]
    for line in lines:
        #print (line)
        if line.find("-----Original Message-----")!=-1 or \
        line.find("----- Forwarded") != -1 or line.find("--------- Inline attachment") != -1 or \
        line.find(">") == 0 or line.find("@ENRON") != -1 or line.find("--------------------------") != -1 or \
        line.find("@ECT") != -1 or line.find("To:")!=-1 or line.find("From:")!=-1:
            break
            
        final.append(line)
        
    #print (final)
    new_row="\n".join(final)
    return pd.Series({'new_content':new_row})