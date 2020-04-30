# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:36:10 2019

@author: Teenu
"""
from Adversary import Adversary
import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/Teenu/Documents/code/spam.csv")
gen=Adversary()
for i, item in enumerate(data['Category']):
    texts.append(data['Message'][i])
    #print(texts)
#   # print(labels)
    #print(i)
    if item == 'ham':
      labels.append(0)
    else:
      labels.append(1)
      
texts = np.asarray(texts)
labels = np.asarray(labels)   
spam_messages=[t for i, t in enumerate(texts) if labels[i] == 1]
texts_gen = gen.generate(spam_messages, text_sample_rate=5.0, word_sample_rate=0.5,
                         attacks={'synonym': 0.5, 'change_case': 0.8, 'letter_to_symbol': 0.5, 'delete_characters': 0.3})   

#df=pd.DataFrame(texts_gen,coloumns=[Message,Label])
#print(df)

#print(texts_gen)
#text_gen.to_csv('hello.csv')
numpy.savetxt("C:/Users/Teenu/Documents/code/foo.csv", texts_gen, delimiter=",")