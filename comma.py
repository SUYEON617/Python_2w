#! /usr/bin/env python

CMA="1,234,567"
a=CMA.split(",")
print(a)

c=''.join(a)
d=int(c)+100
print(d)

b=CMA.replace(',','')
print(int(b)+100)

s=input("separator :")
k=CMA.split(s)
print(k)
