#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python 3.8.2

# 导入依赖包
import pandas as pd
import math
from math import log

# 导入数组
df = pd.read_csv('profile_out.csv')  # DataFrame
df


# In[7]:


# 删除无关行无关列
dfclean = df.drop([0, 1, 2, 3]).drop(columns = ['Unnamed: 3'])

dfclean =  dfclean.reset_index(drop=True)

dfclean = dfclean.set_axis(['x', 'y', 'z'], axis='columns', inplace=False)
dfclean


# In[8]:


#dfclean.dtypes


# In[11]:


# 将xyz转换为浮点型
dfclean['x'] = dfclean['x'].apply(float)
dfclean['y'] = dfclean['y'].apply(float)
dfclean['z'] = dfclean['z'].apply(float)

# 对z列进行取整，视网格大小而定
dfclean['z']=dfclean['z'].map(lambda x:("%.2f")%x)
dfclean


# In[12]:


# 删除列准备对z坐标进行处理
df_z = dfclean.drop(columns=['x', 'y'])

# 去除重复
array_1 = df_z.drop_duplicates()

# 将列z转换为数组
arrayz = array_1["z"].unique()


# In[13]:


#求数组长度
l = len (arrayz)

#第一层网格中心点高度
h0 = 0.0005

#创建空数组
ea1 = []
ea2 = []

for i in range(0, l) :
    
    arrayz[i]
    
    #创建交换空间储存对应z值的行
    swap = dfclean.loc[dfclean['z'] == arrayz[i]]
    
    #提取交换空间中y列到数列
    arrayh = swap["y"].unique()

    #求数组长度
    b = len(arrayh)
    print(b)   
        
    for a in range(0, b) :
                
        #求高度起始值
        h_min = min (arrayh)
        
        #h_min = float (h_min)

        #arrayh[a] = float(arrayh[a])
        
        #求相对高度
        h_ref = abs(float(arrayh[a])-float(h_min))+ h0
        
        #将求解结果写入数组
        ea1.append(h_ref)
        

        #print(h_ref)


# In[14]:


# 对数律速度入口求解
k = 0.41
ustar = 0.9
z0 = 0.1

for c in range(0, len(ea1)):
    v = log(ea1[c]/z0+1)*ustar/k
    ea2.append(v)
    
print (min (ea2))
print (max (ea2))


# In[15]:


ex3 = pd.DataFrame(ea2)
ex3 = ex3.set_axis(['velocity'], axis='columns', inplace=False)


# In[16]:


# 合并dataframe
dffinal = dfclean.join(ex3)
dffinal


# In[17]:


# 将DataFrame写入csv
dffinal.to_csv('Profile_final.csv')


# In[ ]:




