#! /usr/bin/env python
"""
f=open('./dataFile.txt','r')
print(f.read())
f.close()
"""
f=open('./dataFile.txt','r')
for i in f.readlines():
    print(i)
    print(i.rstrip('\n')) #줄바꿈문자 없애주기 방법
#print(f.readlines())
f.close()

"""
f=open('./dataFile.txt','r')
print(f.readline())
print(f.readline())
f.close()
"""
