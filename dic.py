#! /usr/bin/env python

d={'regNum0':'951213-0000000','regNum1':'960125-0000000','regNum2':'970705-0000000'}
d_mon={1:"Jan",7:"Jul",12:"Dec"}

for i in d.keys():
    k=d[i]
    m=k[2:4]
    o=k[4:6]
    print(i, ":", d_mon[int(m)]+"-"+o)

print("regNum0 : ", d_mon[int(d['regNum0'][2:4])], "-", d['regNum0'][4:6])
print("regNum1 : ", d_mon[int(d['regNum1'][2:4])], "-", d['regNum1'][4:6])
print("regNum2 : ", d_mon[int(d['regNum2'][2:4])], "-", d['regNum2'][4:6])

print(d_mon[int(d['regNum1'][2:4])])

for x in d.keys():
    r=d.get(x)
    print(x+":"+d_mon[int(r[2:4])]+"-"+r[4:6])
