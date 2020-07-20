#! /usr/bin/env python

calc='10 USD, 5 EUR, 7 JPY, 9 CNY'

d={'USD':'1,203.82','EUR':'1,365.73','JPY':'11.22','CNY':'172.04'}

b=calc.split(",") #list됨
print(b)

result=[]
for i in range(len(b)):
    k=b[i]
    o=k[:3]
    r=k[3:]
    w=str(round(int(o)*float(d[r].replace(",","")),2))+' KRW'
    result.append(w)
print(result)

