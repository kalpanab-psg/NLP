# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:31:09 2020

@author: bkalp
"""

'''
A part-of-speech tagger, or POS-tagger, processes a sequence of words and attaches a part of speech tag to each word.
 To do this first we have to use tokenization concept . NLTK provides documentation for each tag, which can be queried
 using the tag,
>>> nltk.help.upenn_tagset(‘RB’)
 '''

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
  
 
txt = '''
ONE DAY a man said to Mulla Nasruddin, "I've heard you've got vinegar that is 40 years old."

"That is true," said Hodja.

"Will you give me some?" asked the man.

"If I gave vinegar to all those who asked, it wouldn't have become 40 years old," said Hodja.''' 



# sent_tokenize is one of instances of  
# PunktSentenceTokenizer from the nltk.tokenize.punkt module 
  
tokenized = sent_tokenize(txt) 
for i in tokenized: 
      
    # Word tokenizers is used to find the words  
    # and punctuation in a string 
    wordsList = nltk.word_tokenize(i) 
  
    # removing stop words from wordList 
    wordsList = [w for w in wordsList if not w in stop_words]  
  
    #  Using a Tagger. Which is part-of-speech  
    # tagger or POS-tagger.  
    tagged = nltk.pos_tag(wordsList) 
  
    print(tagged) 
 

#print documentation of CD    
print(nltk.help.upenn_tagset('CD'))
print(nltk.help.upenn_tagset('NNP'))