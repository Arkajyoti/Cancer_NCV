# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:34:52 2017

@author: Arkajyoti Ghoshal
"""
#print('.....................................'*200)
l=[]
import glob

x=glob.glob('G:\Sudhakaran\Datasets\Cosmic All NCV\CosmicNCV_split_2\*tsv')
for i in x:
    with open(i) as csvf:
        for columns in (raw.strip().split() for raw in csvf):  
        #print (columns[1])
            s=[columns[5]]
            for x in s:
                #print(x)
                l.append(x)
final_list=set(l)
print(len(final_list))


for i in final_list:
    #print(i)
    with open('Cancertypes.txt','a') as nf:
        nf.writelines(["%s\n" % i]) #for it in list])

        nf.close()
        