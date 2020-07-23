# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:11:06 2020

@author: kalpana
"""

import nltk

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#state_union is corpus of talks
train_text=state_union.raw('2005-GWBush.txt')
test_text=state_union.raw(r'2006-GWBush.txt')

model_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=model_tokenizer.tokenize(test_text)

def  process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            
            namedent= nltk.ne_chunk(tagged)
            namedent.draw()
    except exception as e:
        print(str(e))
        
process_content()