
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# In[2]:

df1 = pd.read_csv('PCA/PCA_without_poly_Co_fifth.csv', index_col = 0)
df2 = pd.read_csv('PCA/PCA_without_poly_Pt_fifth.csv' , index_col = 0)


# In[3]:

df1_len = df1.shape[0]
df2_len = df2.shape[0]
df2.shape + df1.shape


# In[4]:

X = pd.concat([df1, df2])


# In[5]:

y1 = pd.Series([0]*df1_len)
y1.shape


# In[6]:

y2 = pd.Series([1]*df2_len, index = range(df1_len-1,(df1_len + df2_len)-1))
y2.shape


# In[7]:

y = pd.concat([y1,y2]) 
y.shape


# In[8]:

y.tail()


# In[9]:

X_train, X_test, y_train1, y_test1 = train_test_split(X, y)
y_train = pd.DataFrame(y_train1)
y_test = pd.DataFrame(y_test1)


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[ ]:

# Creating the classifier object
this_C = 10.0
clf = SVC(kernel = 'rbf', C=this_C).fit(X_train, np.ravel(y_train))


# In[ ]:

# Testing with a case

clf.score(X_test,y_test)


# In[ ]:




# In[ ]:




# In[ ]:



