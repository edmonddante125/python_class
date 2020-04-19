# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:24:44 2020

@author: manish
"""
##a=45
##b=76
##print(a+b)
##print(a-b)
##print(a*b)
##print(a/b)
#
#a=23
#b=45
#def art_ops():
#    print("hello")
#    print(a+b)
#    print(a-b)
#    print(a*b)
#    print(a/b)
#art_ops()
#a=10
#b=5
#art_ops()
#def details(usernames,password):
#    print("{} is the username {} is the password".format(usernames,password))
#details("suresh","suresh123")                        
#arbitrary positional arguments:-
#def trans(*a):
#    print(a)
a=34
def add():
    global a 
    global b 
    a=7
    b=67
    print("inside",a)
    print(b)
print("Outside",a)
add()
print(a)

def add(a,b):
    return(a+b)
    
def sub(c):
    return(add(7,8)-c)
sub(4)
#function calling itself is called as recursion...

def fact_cal(a):
    if a==1:
        return 1
    else:
        return a*fact_cal(a-1)
print(fact_cal(8))
def trans(*a,name):
    print("{} amount is being withdrawed from {} account".format(sum(a[0])))

















