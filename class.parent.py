#! /usr/bin/env python

class Cat:
    def __init__(self):
        self.sleepy=True
    def snack1(self):
        print("myeo")

class Ko(Cat): #여기서부터 상속시작
    def setAge(self,Age):
        self.__age=Age #1
        print("set age to {0}.".format(Age))
    def showAge(self):
        print("{0} years old.".format(self.__age)) #1
    def snack2(self):
        print("야옹")
"""
m=Ko()
m.setAge(7)
m.showAge()
print(m.age,end="\n -----------------------------------------------\n")
"""#비공개 속성 안해준 것, #1에서 self.age가 self.__age이렇게 됨. (비공개 속성시)


m=Ko()
m.setAge(7) #setAge 메소드로만 Age가 정해지게끔 한 것. 
m.showAge()
print(m.__age,end="\n -----------------------------------------------\n") #비공개 속성에 직접 접근하려고 시도할 시, 이 속성을  볼 수 없어서  에러남. 볼려면 같은 클래스 내의 메소드만이 해당 비공개 속성을 볼 수 있음. 비공개 속성은 같은 클래스 내에서 공유하는 것.  

"""
m.snack1()
m.snack2()
print(m.sleepy)
"""
#Cat에 있는 메소드와 Ko에 있는 메소드 이름이 겹친다면, Ko 메소드가 실행됨.=>메소드 오버라이딩

