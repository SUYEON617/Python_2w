#! /usr/bin/env python

class Person:
#    nation ='A nation' 이렇게 원래 초기화해줬지만, 밑의 init 메소드로 한다.
    def __init__(self,country):
        self.nation=country
    def showNation(self):
        print("my nation is",self.nation)    

su=Person('Korea') #==> su 생성 -> __init__  돌아감
su.showNation()
