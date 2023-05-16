#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url = "https://quotes.toscrape.com/page/1/"


# In[3]:


response = requests.get(url)


# In[4]:


response.content


# In[5]:


soup = BeautifulSoup(response.content,'html.parser')


# In[6]:


print(soup.prettify())


# In[ ]:





# In[7]:


quote = soup.find_all('div', attrs={'class':'quote'})


# In[8]:


quote


# In[9]:


for i in quote:
    quotes = i.text.strip().split('\n')[0]
    print(quotes)


# In[10]:


for i in quote:
    author = i.find('small',attrs={'class':'author'}).text.strip()
    print(author)


# In[11]:


for i in quote:
    tags = i.find('meta',attrs={'class':'keywords'})
    tags = tags['content']
    print(tags)


# In[12]:


quote = soup.find_all('div', attrs={'class':'quote'})

books = []

for i in quote:
    quotes = i.text.strip().split('\n')[0]
    author = i.find('small',attrs={'class':'author'}).text.strip()
    tags = i.find('meta',attrs={'class':'keywords'})
    tags = tags['content']
    books.append(([quotes,author,tags]))
    
print(books)
    


# In[13]:


books = []

for i in range(1,6):
    url = "https://quotes.toscrape.com/page/1/"
    response = requests.get(url)
    response.content
    soup = BeautifulSoup(response.content,'html.parser')
    quote = soup.find_all('div', attrs={'class':'quote'})
    
    for i in quote:
        quotes = i.text.strip().split('\n')[0]
        author = i.find('small',attrs={'class':'author'}).text.strip()
        tags = i.find('meta',attrs={'class':'keywords'})
        tags = tags['content']
        books.append(([quotes,author,tags]))
 
    


# In[14]:


df = pd.DataFrame(books,columns= ['quotes','author','tags'])


# In[15]:


df


# In[16]:


df.to_csv('SampleQuotes.csv')


# In[17]:


sq = pd.read_csv('SampleQuotes.csv')


# In[18]:


sq.head()


# In[ ]:




