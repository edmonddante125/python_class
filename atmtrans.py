# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:37:09 2020

@author: manish
"""
count=0
while count<3:
    pin=int(input("Enter the pin"))
    acc_type=input("Enter Account Type")
    amount=int(input("Enter the amount"))
    if pin==1234:
#        acc_type=input("Enter Account Type")
        if acc_type=="Saving":
#            amount=int(input("Enter the amount"))
            print(amount," is being debited from your account")
            break
        else:
            print("Account type not matched")
            count+=1
            continue
    else:
        print("incorrect PIN")
        count=count+1
else:
    print("Tried more time ! error")
print("transaction successful")
        