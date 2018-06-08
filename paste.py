# -*- coding: utf-8 -*-
'''
Created on Fri Jun  8 09:55:25 2018

@author: May.gloddemon@gmail.com

假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。
该字符串包含所有表项，表项之间以逗号和空格分隔，
并在最后一个表项之前插入 and。
例如，将前面的 spam 列表传递给函数，
将返回'apples, bananas, tofu, and cats'。
但你的函数应该能够处理传递给它的任何列表。
'''

def paste(List):
    if type(List)==list:
        length=len(List)
        if length==0:
            print('The list has none!')
        elif length==1:
            return str(List[0])
        else:
            s=''
            for i in range(length-1):
                s=s+str(List[i])+','
            s=s+'and '+str(List[-1])+'.'
            return s
    else: 
        print('please input a list!')
