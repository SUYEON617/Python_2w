#! /usr/bin/env python

f=open('./exam.file','r')
k=f.readlines()
#print(k)
for i in range(len(k)):
    if i%2==1:
        print(k[i],end='')
f.close()
