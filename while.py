#! /usr/bin/env python

cnt=input("값을 입력하세요 : ")

#cnt=0

if cnt.isdigit()==False:
    print("숫자를 입력하세요.")
else:
    cnt=int(cnt)
    while True:
        cnt+=1
        if cnt>5:
            print(cnt,"is bigger than 5")
            break
        elif cnt>2:
            print(cnt,"continue!")
            continue
        print(cnt, "test if")
