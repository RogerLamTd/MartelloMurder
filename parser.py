#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt
import time
people=["Veronica", "Jason", "Thomas", "Rob", "Kristina", "Marc-Andre", "Dave", "Salina", "Harrison", "Alok", "Eugene", "James"]


# In[2]:


df = pd.read_json("Data.json")
df = df.transpose()


# In[5]:


veronica = pd.DataFrame({"device": [], "location": [], "event": [], "guest": []})
df.columns = ["device", "location", "event", "guest"]

#for person in people:
#    pdName = str(person+"_events")
#    pdName = pd.DataFrame({"device": [], "location": [], "event": [], "guest": []})
for row in df.itertuples(index=True):
    if (getattr(row,"guest") == "Veronica"):
        veronica.loc[getattr(row,"Index")] = [getattr(row,"device"),getattr(row,"location"),getattr(row,"event"),getattr(row,"guest")]
            


# In[6]:


veronica


# In[ ]:




