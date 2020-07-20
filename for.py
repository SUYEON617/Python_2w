#! /usr/bin/env python
"""
cnt=0
for i in range(5):
    cnt+=1
    print(cnt,"번 실행했음")

print(sum(range(1,5)))
"""
"""
re=[]
for i in range(1,5):
    re.append(i)
print(re)
"""

"""
for i in range(1,5):
    if i==2:
        continue
    cnt+=i
print(cnt)
"""
"""
l=['apple','banana']
for a,b in enumerate(l):
    print(a,b)
#    print('a:',a)
#    print('b:',b)
"""
"""
s='abssddcd'
for i in sorted(s):
    print (i)
"""
"""
dan=input("give me dan : ")

if dan.isdigit()==0:
    print("숫자를 입력하세요.")
else:
    dan=int(dan)
    if dan in range(2,20):
        for i in range(1,10):
            print(dan*i)
    else:
        print("2~19 사이의 숫자로 생각해보세요.")
"""
#다시 입력하게끔 하는 것
while True:
    dan=input("give me dan : ")
    if not dan.isdigit():
        print("다시 입력해주세요.")
        continue
    elif 1<int(dan)<20:
        break
    else:
        print("2~19 사이로 입력해주세요.")
for i in range(1,10):
    print(int(dan)*i)
        
        
