# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#PART1
import nltk
from nltk.tokenize import word_tokenize
file =  open("Sample_Input1.txt","r")
text = file.read()
mod_text ="1"
index=2
for i in range(0,len(text)-3):
    mod_text = mod_text + text[i]
    if(text[i]=='\n' and text[i+1]!=' '):
        mod_text = mod_text + str(index)
        index= index+1

print(mod_text)
    
file.close()


#PART2
def word_freq(text,word):
    freq = 0
    corpus = word_tokenize(text)
    for w in corpus:
        if(word==w):
            freq =freq+1
    return freq



print(word_freq(text,"CAA"))

#Testing if my function is correct
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
fdist = FreqDist()
for word in word_tokenize(text):
    fdist[word] += 1

print(fdist["CAA"])




#PART3

import re

#Data cleaning safai ho zaaye
def clean_text(text):
  text = text.lower()
  text = re.sub(r"i'm","i am ",text)
  #text = re.sub(r".","",text)
  text = re.sub(r"he's","he is ",text)
  text = re.sub(r"she's","she is ",text)
  text = re.sub(r"what's","what is",text)
  text = re.sub(r"where's","where is",text)
  text = re.sub(r"\'ll","will",text)
  text = re.sub(r"\'ve","have",text)
  text = re.sub(r"\'d","would",text)
  text = re.sub(r"won't","would not",text)
  text = re.sub(r"can't","cannot",text)
  text = re.sub(r"[~@#$^&*()<>?/{},.|"";]","",text)
  text = re.sub('[^A-Za-z0-9]',' ',text)                 
  return text

text1 = clean_text(text)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text1)
text2 = [w for w in word_tokens if not w in stop_words] 

from nltk.probability import FreqDist


fdist1 = FreqDist()
for word in text2:
    fdist1[word] += 1

fdist1.most_common(10)




#PART4

word4=[]
for word in word_tokens:
    if(len(word)==4):
        word4.append(word)
        
fdist4 = FreqDist()
for word in word4:
    fdist4[word]+=1

lis=fdist4.most_common()

lis.reverse()
print(lis)

#print(lis[-10:])



#PART5

from nltk.corpus import brown
fdistbrown=FreqDist()
for word in brown.words():
    fdistbrown[word]+=1

freqatleast3 = []
for word in brown.words():
    if(fdistbrown[word]>=3):
        freqatleast3.append(word)
        
print(freqatleast3)





    
