#! /usr/bin/env python
"""
a=input("a: ")
b=input("b: ")

if (a.isdigit() and b.isdigit() and (int(a)<int(b)<10000)):
    a=int(a)
    b=int(b)
    k=[]
    for i in range(a,b+1):
        if i%2==1:
            k.append(i)
    print(sum(k))
else:
    print("error")
"""

while 1:
    a=input("a :")
    b=input("b :")
    if (a.isdigit() and b.isdigit() and int(a)<int(b)):
        break
    else:
        if not (a.isdigit() and b.isdigit()):
            print("숫자를 입력하시오")
        elif not (int(a)<int(b)):
            print("a는 b보다 작아야합니다.")
        continue
k=[]
a=int(a)
b=int(b)
for i in range(a,b+1):
    if i%2==1:
        k.append(i)
print(sum(k))

#result = 0
#result +=i
