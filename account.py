#! /usr/bin/env python
a=input("계좌를 설정하세요 : ")
pwd=input("비밀번호를 입력하세요 : ")
d={'01049229300':[1,8000],'01049229301':[2,9000]}
pwd=d[a][0]
bal=d[a][1]

won1=0
won2=0
won3=0

class Account: 
    def __init__(self):
            self.__password=pwd
            self.__balance=bal
          
    def deposit(self,won1):
        won1=int(input("입금할 금액을 설정하세요:"))
        self.__balance+=won1
        print(self.__balance,"원이 남았습니다.")
        
    def withdrawl(self,won2):
        won2=int(input("출금할 금액을 설정하세요:"))
        self.__balance-=won2
        print(self.__balance, "원이 남았습니다.")

    def transfer(self,won3):
        b=input("받을 계좌를 설정하세요 :")
        won3=int(input("전환할 금액을 설정하세요:"))
        d[b][1]+=won3
        self.__balance-=won3
        print("내 잔액: ", self.__balance, "상대방 잔액 : " ,d[b][1])

    def showBalance(self):
        print("내 잔액 : ", self.__balance)
        


w=Account()
try:
    w.deposit(won1)
    w.withdrawl(won2)
    w.transfer(won3)
    w.showBalance()
except:
    print("error")
