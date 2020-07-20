#! /usr/bin/env python

class Person:
    nation ='A nation'
    def greeting(self):
        print('(Person\'s method) greeting :','Hi')
    def hi1(self):
        self.greeting() #클래스의 메소드에서 클래스의 메소드를 사용하는 방법
    def hi2(self):
        greeting() #클래스의 메소드에서 함수를 사용하는 방법
def greeting():
    print('(normal function) greeting : ', 'Hello')

su=Person()
su.greeting()
print() #공백주기
su.hi1()
su.hi2()

#@@@@@@@@@@@@@@@@@클래스 밖에서 클래스 속성을 바꾸지 말자.@@@@@@@@@@@2
