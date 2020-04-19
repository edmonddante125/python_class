# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:23:59 2020

@author: manish
"""
##a="""python is a programming language 
##Django is a framework."""
##print(a)
#a="Python is a programming"
#print(len(a))
#print(a[-1:-(len(a)+1):-1])
##string methods
#print(dir(str))
a="Pythonisaprogramming3421342"
print(a.startswith('P'))
print(a.isalpha())
#isalnum() checks for alphanumeric values 
print(a.isalnum())
a="Django is A Framework 513"
print(a.islower())
print(a.lower())
print(a.upper())
#title() -- Each and every word starting character is converted to uppercase..
print(a.title())
print(a.swapcase())
print(a.index('o'))
print(a.split())
print(a.split('a'))
a="\n\tpython is used for \n webdevelopment\n"
#strip() --it removes the escape sequences from string at starting and ending

print(a.lstrip())
a="python is a programming language"
print("".join(a.split()))
a="1"
print(a.zfill(15))
a="don't trouble the trouble if you trouble the trouble the trouble troubles you i am not the trouble i am the truth"
print(a.replace('trouble','problem',4))
#"Your order with 123445 order id has been placed successfully. will be delivered by 5 days.."
emp_id=input("enter your id:")
emp_com=input("Enter your company name:")
emp_loc=input("enter Location:")
print("Person with {b} emp id is working at {c} company at {a} location".format(a=emp_loc,b=emp_id,c=emp_com))