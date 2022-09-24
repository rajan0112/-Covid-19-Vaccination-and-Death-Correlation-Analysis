#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Installing the Geopandas
get_ipython().system('pip install geopandas')


# In[2]:


# Installing the Map Classify 
get_ipython().system(' pip install mapclassify')


# In[6]:


# Visualizing Death Data

import geopandas 
import pandas as pd
import matplotlib.pyplot as plt
import mapclassify as mc

#Importing the Shape file of the USA
geo_usa = geopandas.read_file('/Users/rajanpc/Desktop/Project1/STATE_MAP')

#Fitting the Data on the Map of the USA
for i in ['December.csv','March.csv','May.csv','July.csv','Oct.csv','December21.csv']:
    df= pd.read_csv('/Users/rajanpc/Desktop/Project1/STATE_MAP/Death_Data/{}'.format(i))
    gdf = pd.concat([geo_usa, df], axis=1)
    gdf.plot(column='Death', scheme='user_defined', classification_kwds={'bins':[5,15,25,40,60,75,100,135,175,200]}, figsize=(25, 15), legend=True, cmap='OrRd')
    plt.xlim(-130,-55)
    plt.ylim(20,55)
    plt.title('{} - Daily Deaths due to Covid by States'.format(i[:-4]),fontsize=25)
    plt.show()


# In[13]:


# Visualizing Death Data

import geopandas 
import pandas as pd
import matplotlib.pyplot as plt
import mapclassify as mc

#Importing the Shape file of the USA
geo_usa = geopandas.read_file('/Users/rajanpc/Desktop/Project1/STATE_MAP')

#Fitting the Data on the Map of the USA
for i in ['Jan.csv','March.csv','May.csv','July.csv','Sept.csv','December.csv']:
    df= pd.read_csv('/Users/rajanpc/Desktop/Project1/STATE_MAP/Vaccination_Data/{}'.format(i))
    gdf = pd.concat([geo_usa, df], axis=1)
    gdf.plot(column='Vaccination', scheme='user_defined', classification_kwds={'bins':[100000, 150000, 250000, 500000, 1000000, 3000000, 5000000, 7500000, 10000000, 15000000, 25000000, 30000000]}, figsize=(25, 15), legend=True, cmap='Blues')
    plt.xlim(-130,-55)
    plt.ylim(20,55)
    plt.title('{} - Daily Deaths due to Covid by States'.format(i[:-4]),fontsize=25)
    plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_death=pd.read_csv("/Users/rajanpc/Desktop/Project1/Daily_Deaths.csv")
df_death

fig,ax = plt.subplots(figsize=(35, 15))
ax.plot(df_death.Date, df_death.Vaccination, color="blue")

ax.set_xlabel("Date",fontsize=14)
ax.set_ylabel("Total Vaccinations (100 Millions)",color="blue",fontsize=14)
ax.set_ylim(0,500000000)
#ax.set_xlim(0,10)

ax2=ax.twinx()
ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
#ax2.set_xlim(0,10)
ax2.plot(df_death.Date, df_death.Deaths ,color="red")
ax2.set_ylabel("Daily Deaths",color="red",fontsize=14)
ax2.set_ylim(0,4500)

plt.show()

