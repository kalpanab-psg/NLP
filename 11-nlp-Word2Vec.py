# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 05:04:24 2020

@author: kalpana

BOW and TF-IDf
disadv:1)  Gives information on word occurance. But not the imortance of a word in the context,
            which is important for sentiment analysis

        2)Tends to overfitting

Word2Vector each word is represented as a vector of 32 dimensions than a single no
here semantic infrm and relation between word is preserved

"""

import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re
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
 
#preprocess the data
 
text=re.sub('[[0-9]*\]', ' ', speech_text) #remove chars other than alphabets
text=re.sub(r'\s+', ' ', text) # make continuous spaces to single space
text=text.lower()  #change words to lowercase
text=re.sub(r'\d', ' ', text) 
text=re.sub(r'\s+', ' ', text) 

sentences=nltk.sent_tokenize(text)
sentences=[nltk.word_tokenize(sentence) for sentence in sentences]

 

for i in range(len(sentences)):
    sentences[i]=[word  for word in sentences[i] if word not in set(stopwords.words('english'))]
       
#training the model
    
model=Word2Vec(sentences,min_count=1)

words=model.wv.vocab

#finding word vectors
vector=model.wv['vision']

#similar words
simi_wrds= model.wv.most_similar('vision')



     





