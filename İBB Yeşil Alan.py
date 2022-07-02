#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[31]:


green=pd.read_csv(r'C:\Users\ilgaz\OneDrive\Masaüstü\İBB Yeşil Alan Project\yeil-alan-bilgileri.csv')
green.columns =['AÇIK VERİ PLATFORMU GÖSTERGE NOSU','QPR GÖSTERGE ADI','FAALİYET KONUSU','BİRİM','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','']

green.tail(12)


# In[ ]:





# In[32]:


green = green.iloc[4:5 , 4:-2]
print(green)


# In[33]:


result1 = green.iat[0, 1]
result2 = green.iat[0, 2]
result3 = green.iat[0, 3]
result4 = green.iat[0, 4]
result5 = green.iat[0, 5]
result6 = green.iat[0, 6]
result7 = green.iat[0, 7]
result8 = green.iat[0, 8]
result9 = green.iat[0, 9]
result10 = green.iat[0, 10]
result11 = green.iat[0, 11]
result12 = green.iat[0, 12]
result13 = green.iat[0, 13]
result14 = green.iat[0, 14]
result15 = green.iat[0, 15]
result16 = green.iat[0, 16]

result1 = int(result1.replace(',', ''))
result2 = int(result2.replace(',', ''))
result3 = int(result3.replace(',', ''))
result4 = int(result4.replace(',', ''))
result5 = int(result5.replace(',', ''))
result6 = int(result6.replace(',', ''))
result7 = int(result7.replace(',', ''))
result8 = int(result8.replace(',', ''))
result9 = int(result9.replace(',', ''))
result10 = int(result10.replace(',', ''))
result11 = int(result11.replace(',', ''))
result12 = int(result12.replace(',', ''))
result13 = int(result13.replace(',', ''))
result14 = int(result14.replace(',', ''))
result15 = int(result15.replace(',', ''))
result16 = int(result16.replace(',', ''))

print(result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16)
    
    
    


# In[34]:


x = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
y= [result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16]


# In[35]:


def cm_to_inch(value):
    return value/2.54
fig=plt.figure(figsize=(cm_to_inch(25), cm_to_inch(15)))
green=green.replace(',', '')
plt.plot(x, y)
import matplotlib.pyplot as plt
plt.ticklabel_format(style='plain', axis='y')
plt.ylim([0,6345052])
plt.xlabel('Yıllar',fontsize=20, fontweight='bold')
plt.ylabel('Alan miktarı (m2)',fontsize=20, fontweight='bold')
plt.title('İBB Yıl İçinde Yapılan Yeşil Alan Miktarı',fontsize=25, fontweight='bold')
plt.show()



# In[ ]:





# In[ ]:





# In[ ]:




