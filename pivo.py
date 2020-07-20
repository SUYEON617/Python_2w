#! /usr/bin/env python
n=int(input("몇번째까지 : "))

def fivo(n):
    re=[0,1]
    for i in range(n-2):
        k=re[i]+re[i+1] 
        re.append(k) 
#위에 있는  줄이랑 합쳐서 => re.append(re[-1]+re[-2])
    return sum(re),re,re[n-1] #re[n-1]=re[-1]; 마지막 element만  나오게 하는 거
    
#print(fivo(n))

A,B,C=fivo(n)
print(str(A)+'\n'+str(B)+'\n'+str(C)) #한줄씩 써주기 위해서 진행
