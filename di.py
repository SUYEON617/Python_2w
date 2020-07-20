#! /usr/bin/env python

s='We tried list and we tried dicts also we tried Zen'
k=s.split(" ")

#print(k)

d={}

for i in k:
    d[i]=str(k.count(i)) #주석처리된 join 쓰려면 str필요

"""이렇게 써도 동일함 참고
for i in k:
    if i not in d:
        d[i] =1
    else:
        d[i]+=1
print(d)
"""

"""
for x in d.items():
    s=' '.join(x)
    print(s)
"""
for x in d.keys():
   print(x,d[x])

"""강사님 풀이
import collections
cnt=collections.Counter(s)
print(cnt)
---------------------------
set 관련 연산
A=['a','b','a','c','d','f']
B=['b','c','b','d','e','e','e']
C=['q','w','e','r','t','y','y','y']
a_cnt=collections.Counter(A)
b_cnt=collections.Counter(B)
c_cnt=collections.Counter(C)

print(A)
print(B)
print(C)
print(a_cnt)
print(b_cnt)
print(c_cnt)

a_cnt['a']+=5 #5가 더해진 상태로 반환됨
print(a_cnt|b_cnt) #a_cnt와 b_cnt의 합집합 #count값이 제일 큰 값 순으로 element가 정렬되어 나옴.
print(a_cnt&b_cnt) #둘 다 가지고 있어야 출력됨. counter 두개에서 공통적으로 나와있는 것. count 수는 공통된 것의 숫자만 나옴. b가 2가 아닌 1이 나옴.
# +도, -도 가능

"""
