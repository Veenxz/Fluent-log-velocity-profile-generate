#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math
from math import log

# 导入数组
df = pd.read_csv('1.csv')  # DataFrame

# 清洗数据，删除无关列
dfclean = df.drop(columns=['y-coordinate', 'x_velocity', 'y_velocity', 'z_velocity'])

# 提取一列数据
# df["y"].unique()
# 去除重复
# df.duplicated()
# df.drop_duplicates()


# In[2]:


# 删除列
df_z = dfclean.drop(columns=['x', 'y'])

# 去除重复
array_1 = df_z.drop_duplicates()

# 将列z转换为数组
arrayz = array_1["z"].unique()


# In[3]:


# 求数组长度
l = len(arrayz)

# 创建空数组
ea1 = []
ea2 = []

for i in range(0, l):

    arrayz[i]
    
    # 创建交换空间储存对应z值的行
    swap = dfclean.loc[dfclean['z'] == arrayz[i]]
    
    # 提取交换空间中y列到数列
    arrayh = swap["y"].unique()

    # 求数组长度
    b = len(arrayh)
          
    for a in range(0, b):
        
        # 求高度起始值
        h_min = min(arrayh)

        arrayh[a]
        
        # 求相对高度
        h_ref = abs(arrayh[a]-h_min)
        
        # 将求解结果写入数组
        ea1.append(h_ref)


# In[4]:


k = 0.41
ustar = 2.0
z0 = 0.5

for c in range(0, len(ea1)):
    v = log(ea1[c]/z0+1)*ustar/k
    ea2.append(v)


# In[5]:


ex3 = pd.DataFrame(ea2)
ex3 = ex3.set_axis(['velocity'], axis='columns', inplace=False)


# In[6]:


# 添加新列并赋值
# dfclean['velocity']='ea1'

# dffinal = dfclean.merge(ex3, left_on='x', right_on='velocity', suffixes=('_left', '_right'))

# 合并dataframe
dffinal = dfclean.join(ex3)
dffinal


# In[7]:


# 将DataFrame写入csv
dffinal.to_csv('velocit.csv')


# In[ ]:




