#! /usr/bin/env python
class Coffee(): 
    numCoffee = 10 #클래스 안의 변수 = 속성
    def Hello(self): #클래스 안의 함수 = 메소드. Hello 메소드. self로 매개변수 넣어줘야함.
        print("Hello!")
        return "Hi!"
"""
group1=Coffee() #Coffee class의 instance = group1
print(group1.numCoffee)
group1.Hello()
print(group1.Hello())
"""
class Person():
    nation="A nation"
    def greeting(self):
        print('greeting')
    def printnation(self):
        print(self.nation)
    def changenation(self,target):
        print('change nation : from %s to %s' % (self.nation, target))
        self.nation=target
        print('current nation : {0}'.format(target))
su=Person()
su.greeting()
su.printnation()
su.changenation('Korea')

if isinstance(su,Person):
    print("su is Person")
else:
    print("su is not Person")

out1=isinstance(1,int)
print(out1)
out2=isinstance("hello, it's me",(str,int))
print(out2)

