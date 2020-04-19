# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:08:38 2020

@author: manish
"""
a={"username":"ramesh","password":"ramesh123","emails":["ramesh123@gmail.com","ramesh@gmail.com"]}
print(a.keys())
print(a.items())
a={"username":"ramesh",'password':'ramesh123'}
b=a
print(a)
print(b)
a['email']="ramesh@gmail.com"
print(dir(set))
#task
a=input("Enter your string:-")
b=input("enter your character")
count=0
print(a.count(b))
#task2
a=int(input("Enter your number:-"))
for j in range(2,a+1):
    sample="{}".format(j)*j
    print("*".join(sample),"=",j**j)