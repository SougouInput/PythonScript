# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:55:25 2018

@author: May.gloddemon@gmail.com
"""

def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2        
    elif number%2==1:
        print(3*number+1)
        return 3*number+1        
        
print('please input a number:')
while True:
    try:
        num=int(input())
        result=collatz(num)
        if result==1:
            break
        else:
            continue
    except ValueError:
         print('please input a number not string!')