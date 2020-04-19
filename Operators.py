# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:44:52 2020

@author: manish
"""
#Arithmetic operators
a=14/3
print(a)
b=145%3
print(b)
c=14//3
print(c)
print(14**3)
print(2**2)

#Relational Operators

print(23==23)
print(23!=23)
print(23>=23)
print(23<=23)

#Logical Operators

a=True
b=False 
print(a and b)
print(a or b )
print(not(a))
a=34
b=56
print(a>50 and b<50)

#Assignment Operators 
a+=10

#Membership Operators 
a="python is a programming language"
print("n" in a and "o" in a )
print("Program" in a)
print("Program" not in a)

#Identity Operators 
a=23
b=23
print(a is b)
a="Python"
b="Python"
print(a is b)
a=(1,2,3)
b=(1,2,3)
print(id(a))
print(id(b))
print(a is b)
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)

#Bit Wise Operators
a=23
b=34
print(a&b)
print(a|b)
print(a^b)
#Bit Wise Left Shift(<<)
a=23
print(a<<1)
#Bit Wise Right shift(>>)
a=23
print(a>>1)
#Bit Wise not
a=23
print(~a)