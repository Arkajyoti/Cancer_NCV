# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 23:46:53 2017

@author: Arkajyoti Ghoshal
"""


import csv
import pandas as pd
#import glob

#x=glob.glob('G:\Sudhakaran\Datasets\Cosmic All NCV\dumyf\*tsv')
#print(x)

list1 = []
list2 = []
k = 0

for l in range(1580):

 fp1 = 'G:\Sudhakaran\Datasets\Cosmic All NCV\CosmicNCV_split_2\\CosmicNCV_'+str(l+1)+'.tsv'
 df=pd.read_csv(fp1,delimiter='\t')
#    print(df)

 list2 = list(df.loc['Sample name':'PUBMED_PMID'])


 for i in range(9999):
    if k%100000 == 0:
        j = 0
    if df.iloc[i,3]=='skin':
        
            list1 = list(df.ix[i])
            path = 'skin'+str(k//100000)+'.csv'
            #path='new2.csv'
            with open(path,"a", newline = '') as fp:
                    
                    writer = csv.writer(fp)
                    if j == 0:
                        writer.writerow(list2) 
                        j = 1
                    writer.writerow(list1)
                    k = k+1
           
        
        
            