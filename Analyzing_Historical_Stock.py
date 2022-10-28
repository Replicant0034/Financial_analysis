#!/usr/bin/env python
# coding: utf-8

# # Analyzing Historical Stock/Revenue Data and Building a Dashboard

# In[10]:


import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup 
import requests 


# ### Extracting Tesla Stock Data

# In[4]:


tsla = yf.Ticker("TSLA")
tsla_data  = tsla.history(period="max")
tsla_data.reset_index(inplace=True)
tsla_data.head()


# In[5]:


tsla_data.tail()


# ###  Extracting Tesla Revenue Data

# In[14]:


url = " https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# In[57]:


tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in  soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
tesla_revenue.head()


# In[17]:


tesla_revenue.tail()


#  ### Extracting GameStop Stock Data

# In[18]:


gme = yf.Ticker("GME")
gme_data  = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()


# In[19]:


gme_data.tail()


# In[20]:


url_2 = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_2 = requests.get(url_2).text
soup_2 = BeautifulSoup(html, "html.parser")

for link in soup_2.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# ### Extracting GameStop Revenue Data 

# In[25]:


gme_revenue.head()


# In[26]:


gme_revenue.tail()


# In[49]:


gme_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in  soup_2.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
    


# ### Plot GameStop Stock Graph

# In[41]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[51]:


make_graph(gme_data, gme_revenue, 'gme')


# ### Plot Tesla Stock Graph

# In[58]:


tesla_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in  soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)


# In[59]:


tesla_revenue.tail()


# In[60]:


make_graph(tsla_data, tesla_revenue, 'tsla')


# In[ ]:




