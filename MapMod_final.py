# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:40:21 2017

@author: Arkajyoti Ghoshal
"""

Genefile='SmH.csv'
import pandas as pd

df1 = pd.read_csv(Genefile, delimiter = ',')

for k in range(263):
    mutfiles = 'Breast_split\\breast'+str(k)+'.csv'
    df2 = pd.read_csv(mutfiles)

    for i in range(len(df1.index)):
        for j in range(i,len(df2.index)):
            print(i,j)
            if str(df1.iloc[i,3]) == str(df2.iloc[j,20]):
                if int(df1.iloc[i,4])<= int(df2.iloc[j,21]) and int(df1.iloc[i,5])>= int(df2.iloc[j,22]):
                    print('Gene on chromosome',int(df1.iloc[i,3]),'starts at',int(df1.iloc[i,4]),'ends at', int(df1.iloc[i,5]), 'and has mutation from', int(df2.iloc[j,21]),int(df2.iloc[j,22]))
    
    print(k+1)    