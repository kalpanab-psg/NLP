# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:39:32 2020

@author: kalpana
"""

from nltk.stem import WordNetLemmatizer

from nltk.stem import PorterStemmer

## try stemming first

print('-'*10,'stemming first--sometimes no meaningful stem')

ps=PorterStemmer()
print(ps.stem('goes'))
print(ps.stem('cats'))
print(ps.stem('going'))
print(ps.stem('gone'))
print(ps.stem('googly'))
print('-'*30,'lemmatize')

##lematizer gives meaningful stem
lm=WordNetLemmatizer()
print(lm.lemmatize('goes'))
print(lm.lemmatize('cats'))
print(lm.lemmatize('going'))
print(lm.lemmatize('gone'))
print(lm.lemmatize('googly'))

#printing options
print('-'*20,'options to print verb,adverb etc')

#default noun

print(lm.lemmatize('gone', pos='a'))
print(lm.lemmatize('gone', pos='v'))