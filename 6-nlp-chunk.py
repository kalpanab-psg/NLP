# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:37:26 2020

@author: kalpana
"""
import nltk
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import matplotlib.pyplot as plt

text='We saw a golden retreiver and a small boy in the park'
 


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(text)
print(sent)
#Our chunk pattern consists of one rule, that a noun phrase, NP,
# should be formed whenever the chunker finds an optional determiner, DT,
# followed by any number of adjectives, JJ, and then a noun, NN.


# name the pattern we catch with a word like chunk followed by regexp

pattern = 'chunk: {<DT>?<JJ>*}'


#create a chunk parser and test our sentence
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

#can draw a tree
