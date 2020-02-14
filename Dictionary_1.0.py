#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import difflib
from difflib import get_close_matches

data=json.load(open('data.json'))


# In[2]:


def wordcheck(word):
    word=word.replace('3','e')
    word=word.replace('0','o')
    word=word.replace('1','l')
    word=word.replace('4','a')
    
    return word


# In[3]:


def getdef(word):
    word=word.lower()
    
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print('Did you mean this ==> '+get_close_matches(word,data.keys())[0])
        decide=input('press y for yes and n for no ==> ')
        if decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=='n':
            return('The Word is not found, Please try again!')
        else:
            return('you have entered the wrong input! Please try again!')
    
    else:
        print('The Word is not found, Please try again!')


# In[4]:


word=''

while(True):
    word=input('What word would you like to know of? ==> ')
    
    if(word=='-1'):
        break
        
    word=wordcheck(word)
    
    output=getdef(word)
    
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output+'\n')


# In[ ]:




