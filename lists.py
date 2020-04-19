# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:19:52 2020

@author: manish
"""

#a=[2,3.4,4.5,23,78,12,83]
##print(a[2][4])
###print(a[-1])
##a[0]="P"
##print(a)
##a.append([11,12,13])
##print(a)
###extend()-- It is for adding multiple elements into the lists at last..
##a.extend(['django','aws','devops'])
##print(a)
#
##a.insert(2,'aws')
##print(a)
##a=[]
##for j in range(1,11):
##    a.append(j)
##print(a)
#a.sort()
#print(a)
my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)
