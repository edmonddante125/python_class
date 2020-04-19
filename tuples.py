# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:13:13 2020

@author: manish
"""

a=(1,5,5.6,'python',[11,12,13])
print(type(a))
print(a[4][1])
#tuples are immutable data types
print(a.index(5))
#basic operations:concatenation , repetition 
print((11,12,13,14)+("python",'devops','aws','Datascience'))
print(a)
a[4].append(14)
print(a)
a=("user","workbook")
print(list(a))
a=("23421312312","98997989098997","34534584359843","4324943503")

     