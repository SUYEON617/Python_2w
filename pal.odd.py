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
if len(a)%2==0:
    for i in range(int(len(a)/2)):
        if a[i]==o[i] :
            re.append(a[i])
        else:
            rem.append(a[i])
else:
    for i in range(round(len(a)/2-1)):
        if a[i]==o[i] :
            re.append(a[i])
        else:
            rem.append(a[i])
#print(re)
#print(rem)        
if len(rem)==0:
    print(seq,"is a palidromic seq")
else:
    print(len(rem)*2,"bases differ")
    print(seq,"is not a palindromic seq")
"""
while True: 
    for i in range(len(a)):
        if a[i]==o[i]:
            continue
    print(seq,"is a palindromic seq")
"""
