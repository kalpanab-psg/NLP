# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 05:04:24 2020

@author: kalpana

TF-IDF: Formula  

TF=    no. of rep. of a word in sentence
     -----------------------------------
        no of words in the sentence
     
     
                      ( no. of sentences)
 IDF =     log (---------------------------------------   )
                   (no of sentences containing  the word)

Finally TF * IDF

if we have three sentences

s1=she is a good girl
s2=he is a good boy
s3= all boys and girls are good
   TF               s1            s2         s3
  boy             0             1/2         1/3           
  girl            1/2           0           1/3
  good            1/2           1/2         1/3
  
  
  IDF
  
  boy    log(3/2)
  girl   log(3/2)
  good   log(3/3)
  
  calculate TF* IDF
          f1                f2                           f3
          boy              girl                          good
          
  s1      0              1/2 * log(3/2)                  1/2 * 0
  s2     1/2 *log(3/2)        0                           1/2 * 0
  s3      1/3 * log(3/2)   1/3 * log(3/2)                 1/3 * 0


o/p is the vector of 1's and 0's .
Adv:  We   know the number  of times word occurs in the sentence. 
So importance of a word  in terms of context for sentiment analysis can be used

"""

import nltk

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

import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps=PorterStemmer()
lm=WordNetLemmatizer()

sentences=nltk.sent_tokenize(speech_text)
corpus=[]
for i in range(len(sentences)):
    temp=re.sub(r'[^a-zA-Z]', ' ', sentences[i]) #remove chars other than alphabets
    temp=temp.lower()  #change words to lowercase
    temp=temp.split()
    temp=[ps.stem(word) for word in temp if word not in set(stopwords.words('english'))]
    temp=' '.join(temp)
    
    corpus.append(temp)
    
#for creating TF-IDF model use scikit learn
from sklearn.feature_extraction.text import TfidfVectorizer

cv= TfidfVectorizer(max_features=1500)

'''
The corpus contains a list of 14 sentences.
We create a array of numbers in X which is TF-IDF vector for the 14 sentences in the corpus
'''

X=cv.fit_transform(corpus).toarray()





