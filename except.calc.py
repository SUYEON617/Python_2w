#! /usr/bin/env python
"""
def calc(i1,i2):
    return i1+i2

num1=input('num1 :' )
num2=input('num2 :')
#예외 처리 방법
try:
#    num1=int(num1)
    num1=num1[3939000] #두번째 에러 상황을 만들어보자.
    num2=int(num2)
except ValueError:
    print("value error occured")
except :
    print("다른 에러가 발생")

#result=calc(num1,num2)
"""

num1=input("give age : ")
if not num1.isdigit():
    raise Exception(' pleaseGiveString ' )#error 메세지 커스텀



