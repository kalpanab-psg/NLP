# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:17:03 2020

@author: bkalp
"""


# import these modules 
from nltk.stem import PorterStemmer 
 
   
ps = PorterStemmer() 
  
# choose some words to be stemmed 
words = ["program", "programs", "programer", "programing", "programers"] 
  
for w in words: 
    print(w, " : ", ps.stem(w)) 
    
    
    
#example with speech
    
from nltk.tokenize import word_tokenize, sent_tokenize
speech_text='''
  I have met, so far, 11 million youth like you in a decade?s time, in India and abroad. I have seen their hopes, 
  experienced their pains, walked with their aspirations and heard through their despair. All this experience made me 
  learn something about them, which I would like to share with you:I learnt, every youth wants to be unique, that is, YOU! But the world all around you, is doing its best, day and night, to make you just "everybody else".
Being like everybody else is convenient at the first glance, but not satisfying in the long vision.
The challenge, therefore, my young friends, is that you have to fight the hardest battle, which any human being
 can ever imagine to fight; and never stop fighting until you arrive at your destined place, that is, a UNIQUE YOU!
Being unique will require excellence, let us understand what is excellence in more detail.
Excellence is a self-imposed self-directed life-long process
Excellence is not by accident. It is a process, where an individual, organization or nation, continuously strives 
to better oneself. The performance standards are set by themselves, they work on their dreams with focus and are
 prepared to take calculated risks and do not get deterred by failures as they move towards their dreams. 
Then they step up their dreams as they tend to reach the original targets.
 They strive to work to their potential, in the process, they increase their performance thereby multiplying further their
 potential and this is an unending life cycle phenomenon. They are not in competition with anyone else, but themselves.
 That is the culture of excellence.  

'''
ps = PorterStemmer() 
   
 
words = word_tokenize(speech_text) 

stem_words=[]
   
for w in words: 
    
    stem_words.append( (w,ps.stem(w)) )
