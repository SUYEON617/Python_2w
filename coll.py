#! /usr/bin/env python

s='We tried list and we tried dicts also we tried Zen'
l=s.split(" ")
import collections
cnt=collections.Counter(l)
print(cnt)


A=['a','b','a','c','d','f']
B=['b','c','b','d','e','e','e']
C=['q','w','e','r','t','y','y','y']
a_c=collections.Counter(A)
b_c=collections.Counter(B)
c_c=collections.Counter(C)

"""
print(A)
print(B)
print(C)
"""
print(a_c)
a_c['a']+=5 #a의 count수가 5가 늘어남.

print(a_c)
print(b_c)
print(c_c)

print("|",a_c|b_c)
print("&",a_c&b_c)
#더하기 빼기도 가능(만약 a-b에서 b에 있는 개수가 더 많을 경우, 그냥 없는 걸로 됨)




