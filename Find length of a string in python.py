#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Python code to demonstrate string length
# using for loop
 
# Returns length of string
def findLen(str):
    counter = 0   
    for i in str:
        counter += 1
    return counter
 
 
str = "Python"
print(findLen(str))


# In[6]:


# Python code to demonstrate string length
# using while loop.
 
# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
 
str = "Python"
print(findLen(str))


# In[7]:


# Python code to demonstrate string length
# using join and count
# Returns length of string
def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
 
str = "Python"
print(findLen(str))


# In[8]:


# Python code to demonstrate string length
# using reduce
 
import functools
def findLen(string):
    return functools.reduce(lambda x,y: x+1, string, 0)
 
 
# Driver Code
string = 'Python'
print(findLen(string))


# In[ ]:




