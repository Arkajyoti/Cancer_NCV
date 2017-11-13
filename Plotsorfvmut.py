# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:27:26 2017

@author: Arkajyoti Ghoshal
"""

#import csv
import pandas as pd
Mp= 'Map.csv'
df1 = pd.read_csv(Mp, delimiter = ',')
gn=df1['Gname']
#print(gn)

#from collections import Counter as C
#for i in gn:
    #print(i,Counter(i))
        #print(ct)
    

#nln = [l + [str(counts[l[1]])] for l in lines]
#print(nln)
keys=set(gn)
gname=[]
number=[]
idd=[]
for ii in keys:
    #print(ii)
    xx = 0
    for ij in range(len(gn)):
        if ii==df1.iloc[ij,0]:
            xx=xx+1
    #print(ii,xx)
    gname.append(ii)
    number.append(xx)
for zz in range(len(gname)):
    idd.append(zz)
    
    
print(idd)
import matplotlib.pyplot as plt
import numpy as np
#plt.plot(gname,number)
#plt.show()
plt.xticks(idd,gname)
plt.plot(idd,number)
plt.xticks(range(2),gname, rotation=90)
plt.show()