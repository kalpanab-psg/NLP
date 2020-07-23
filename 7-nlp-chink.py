# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:01:04 2020

@author: kalpana
"""
import nltk
 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
 

text='We saw a golden retreiver and a small boy in the park'
 


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(text)
print(sent)
 

#from our chunk we need to chink what we dont need . see usage of reverse paranthses }{ for chinking 
pattern = """chunk: {<.*>+} 
                     }<VBD|IN|DT>+{ """

#in the above line we take all characters remove verb,in and determinant
                     
#create a chunk parser and test our sentence
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

#can draw a tree
cs.draw()
