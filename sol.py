
import pandas as pd
import numpy as np
import string
data = pd.read_csv('amazon_flip_review.csv')
print(data.shape)


class text_gen:
    
       
        
    def remove_punctuations(text):
        p = set(string.punctuation)
        text = text.lower()
        words=text.split()
        ctext=[]
        for i in range(10):
            p.add(str(i))
        for i in words:
            t = ''.join([x for x in i.encode("ascii","ignore").decode("ascii") if x not in p])
            ctext.append(t)
        return " ".join([i for i in ctext])
    print(string.punctuation)
    uncleaned = [i for i in data.review]
    cleaned = []
    for i in uncleaned:
        try:
            ctxt = remove_punctuations(i)
            if len(ctxt)==0: raise()
            cleaned.append(ctxt)
        except:
            cleaned.append("NAN")
    data['cleanedText'] = cleaned
    data.to_csv(r'amazon_flip_review_cleaned.csv')
        
data = pd.read_csv('amazon_flip_review_cleaned.csv')

data.drop(data[data['cleanedText']=="NAN"].index,axis=0,inplace=True)
data = data.reset_index(drop=True)
print(data.shape)
data.to_csv(r'Final.csv')
