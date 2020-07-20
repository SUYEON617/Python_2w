#! /usr/bin/env python

lang0=["Python","JAVA"]
lang1=["C","C++","VB"]
lang0.extend(lang1)
print(lang0)
#totalLang=lang0+lang1
#print(totalLang)

print(tuple(lang0))

a=[4, 700, 8]
a.append(9)
print(a)
a.sort()
print(a)

wait=[1,2,3,4,5]
print(len(wait))
wait.append(len(wait)+1) #wait[-1]
print(wait)

for i in wait[:]: #[:] 없을 경우, 메모리 주소 문제때문에 제대로 안나옴
    w=wait.pop(0)
    print("{0}번 손님".format(w))
