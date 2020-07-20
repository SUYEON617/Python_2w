#! /usr/bin/env python

r=int(input("반지름을 입력하세요 : "))

def area(r):
    pi=3.141592 #이해하기 쉽게 상수 설명!
    result=2*r*pi 
    return result
print(area(r))

#A,B=area(r)
#print(A,B)
