# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:51:16 2017

@author: Arkajyoti Ghoshal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:27:26 2017

@author: Arkajyoti Ghoshal
"""

#import csv
import pandas as pd
import csv
Mp= 'Map.csv'
df1 = pd.read_csv(Mp, delimiter = ',')
gn=df1['Gname']
pn=df1['ID_SAMPLE']
ss=zip(gn,pn)
ln=list(ss)
#print(ln)
#print(gn)

#from collections import Counter as C
#for i in gn:
    #print(i,Counter(i))
        #print(ct)
    

#nln = [l + [str(counts[l[1]])] for l in lines]
#print(nln)
keys=set(ln)
gname=[]
number=[]
idd=[]
idi=[]
nump=[]
A=ln.sort()
for ii in keys:
    #print(type(ii))
    xx = 0
    for ij in range(len(ln)):
        if ii==ln[ij]:
            xx=xx+1
            idd.append([ln[ij],xx])
            idi.append(xx)
            #with open('Plt.csv', 'a') as f:
               # writer=csv.writer(f)
               # writer.writerow(ln)
            if xx==6:
                print(ii,xx)
for zz in range(len(ln)):
    nump.append(zz)
    
    #print(idd)
import matplotlib.pyplot as plt
#import numpy as np
plt.xticks(nump,ln)
plt.hist(nump,idi)
plt.xticks(range(0),ln, rotation=90)
plt.show()