# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:38:14 2020

@author: manish
"""
#if statements
'''
if condition:
	statements 
'''
#a=56
#if( a>50):
#	print(a," is greater than 50")
#print("Hello")
##if-else 
#emp_id=int(input("Enter the employee id:-"))
#if emp_id==100:
#	print("Punched Successfully")
#else:
#	print("Punching Unsuccessfully")
#if-elif-else statements :
experience=int(input("enter years of experience"))
if experience>6 and experience<=50:
	print("Based on the experience you are a Senior Developer")
elif experience>3 and experience<=6:
	print("Based on the experience you are a Associate Developer")
elif experience>0 and experience<=3:
	print("Based on your experience you are a entry level Developer")
else:
	print("enter a valid number of experience")


