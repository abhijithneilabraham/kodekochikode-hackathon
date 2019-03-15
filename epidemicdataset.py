#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:01:28 2019

@author: abhijithneilabraham
"""

import csv
import random
with open('dataset.csv', 'w') as csvfile:
    fieldnames = ['Diarrhea', 'Fever','Dehydration','Nausea','Appetite Loss']
    
        
    print(fieldnames)       
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    x1=random.randint(1,5)
    x2=random.randint(1,5)
    x3=random.randint(1,5)
    x4=random.randint(1,5)
    x5=random.randint(1,5)
    p=(5*x1)+4*x2
    
    writer.writeheader()
    
    for i in range(0,255):
        dic={'Diarrhea':R[i],'Green':G[i],'Blue':B[i],'index':i}
        
        writer.writerow(dic)