#! /usr/bin/env python

seq=input("seq를 입력하세요 : ")
a=list(seq)
#print(a)

rev=seq.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
o=list(rev)
o.reverse()
#print(o)

re=[]
rem=[]
for i in range(len(a)):
    if a[i]==o[i]:
        re.append(a[i])
    else:
        rem.append(a[i])
if len(rem)==0:
#    print(re); 확인용
    print(seq,"is a palidromic seq")
else:
    print(len(rem),"bases differ")
    print(seq,"is not a palindromic seq")
"""
while True: 
    for i in range(len(a)):
        if a[i]==o[i]:
            continue
    print(seq,"is a palindromic seq")
"""
