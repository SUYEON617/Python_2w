#! /usr/bin/env python

num0=input("num0 : ")
num1=input("num1 : ") #첫번째 함수쓰려면 num0와 num1 앞에 int 붙여줘야
op=input("op : ")
"""
def calc(num0,num1,op):
    if op=="+":
        return num0+num1            
    elif op=='-':
        return num0-num1
    elif op=='*':
        return num0*num1
    elif op=='/':
        return num0/num1
"""
#강사님 풀이 - eval 사용
def calc(num0,num1,op):
    result=eval(num0+op+num1)
    return result
result=calc(num0,num1,op)
print('{} is result.'.format(result)) #시간절약

#print(calc(num0,num1,op))

