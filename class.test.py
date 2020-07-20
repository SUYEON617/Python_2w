#! /usr/bin/env python

d_persons={'Gullaume':'Cananda','Niklas':'Germany','Mark':'USA','Alex':'Swiss','Alberto':'Italia'}

class Person():
    nation="A nation"
    name="username"
    def setName(self,target):
        self.name=target
        print("name:", self.name)
    def setNation(self, target):
        self.nation=d_persons[target]
        print("nation : ", self.nation)

k=Person()
n=input("이름을 입력하세요 (Gullaume, Niklas, Mark, Alex, Alberto)   :      ")
k.setName(n)
k.setNation(n)

"""
list_person=[]

for i in range(len(d_persons)):
    list_person.append(Person())
    list_person[i].setName(list(d_persons.keys())[i])
    list_person[i].findNation(d_persons)

for i in range(len(d_persons)):
    list_person[i].showname()
    list_person[i].showNation()
    print() 
"""

class Persons():
    s_str1='str1'
    s_str2='str2'
    def prtStr(self): #제약조건 넣어서 더해주기
        out=self.s_str1+self.s_str2
        print(out)
    def shows_str1(self): #뒤에서 print(p.s_str1)라고 쓰는 것보다 메소드 이용해서 보는 게 클래스 이용법
        print(self.s_str1)

p=Persons()
#p.s_str1+='aa'=> 이렇게 쓰는 건 클래쓰 쓰는 목적과 다름. 클래스는 클래스 변수들을 자신이 가지고 있고, 메소드도 자신이 가지고 있음. 웬만해서는 모든 연산들이 그 클래스 안에서만 끝나야 한다. 왜? 클래스 속성에 접근하는 함수는 해당 클래스의 메소드여야만 한다. 만약 이렇게 맘대로 바꿔버리면 클래스 목적과 다르기 때문에, 지양해야 한다.
#따라서 접근 못하게 속성을 숨겨버리는 방법을 사용함. => class.greeting.py 진행
p.shows_str1()
p.prtStr()
