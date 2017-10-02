# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:00:09 2017

@author: Arkajyoti Ghoshal
"""
import pandas as pd

#df = {}
for kk in range(262):
    l=[]
    start=[]
    stop=[]
    chrn=[]
    path='G:\Sudhakaran\Codes n Results\Breast\breast'+str(kk)+'.csv'
    df=pd.read_csv(path)
#df = df.convert_objects(convert_numeric=True)
#for i in range(3):
    c=df['genome position']
    
    for i in c:
        l.append(i)    
#print(l)

    for i in range(len(df.index)):
        c=l[i].split(':')
        chrn.append(c[0])
        xc=c[1].split('-')
       
    #print(xc)
        start.append(int(xc[0]))
        stop.append(int(xc[1]))
        #print(chrn,start,stop)

    
      
    #df.insert(20,'ChrN',chrn)
    df.insert(20,'ChrN',chrn)       
    df.insert(21,'Strt',start)
    df.insert(22,'Stop',stop)  
    
    #df2=df1.insert(21,'Strt',start)
    #df3=df2.insert(22,'Stop',stop)
#print(df)
#writer = pd.ExcelWriter(path, engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Sheet1')

#writer.save()
    df.to_csv(path, sep=',', index = False)
    
    
