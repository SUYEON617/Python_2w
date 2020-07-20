#! /usr/bin/env python

calc='10 USD, 5 EUR, 7 JPY, 9 CNY' 
d={'USD':'1,203.82','EUR':'1,365.73','JPY':'11.22','CNY':'172.04'}

b=calc.split(",") #list됨
print(b)

for i in range(len(b)):
    n=b[i][:3]
    m=b[i][3:]
    print(round(float(d[m].replace(",",""))*int(n),2),'KRW', end=" ")
print("\n")


#if b[0][3:6]=="USD":
#    print(round(float(d["USD"].replace(",",""))*int(b[0][0:3]),1),"KRW")
#else: 
#    print("")

#if b[1][3:6]=="EUR":
#    print(round(float(d["EUR"].replace(",",""))*int(b[1][0:3]),2),"KRW")
#else:
#    print("")
#if b[2][3:6]=="YPY":
#    print(round(float(d["EUR"].replace(",",""))*int(b[2][0:3]),2),"KRW")
#else: 
#    print("")
#if b[3][3:6]=="CNY":
#    print(round(float(d["CNY"].replace(",",""))*int(b[3][0:3]),2),"KRW")
#else: 
#    print("")
