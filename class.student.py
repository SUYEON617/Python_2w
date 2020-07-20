#! /usr/bin/env python

kor=int(input("국어 점수 :"))
eng=int(input("영어 점수 :"))
mat=int(input("수학 점수 :"))

class Student:
    def __init__(self,kor,eng,mat): 
        self.__korean=kor
        self.__english=eng
        self.__math=mat
    def showKorean(self):
        print(self.__korean)
    def showEnglish(self):
        print(self.__english)
    def showMath(self):
        print(self.__math)
    def showAverage(self):
        print("평균점수 : ", (self.__korean + self.__english + self.__math)/3)
"""
    def show(self):
        totalscore=self.__korean
        totalscore+=self.__english
        totalscore+=self.__math
        totalscore/=3
        print("평균:" , totalscore)
"""

p=Student(kor,eng,mat)
p.showKorean()
p.showEnglish()
p.showMath()
p.showAverage()     
