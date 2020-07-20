#! /usr/bin/env python
"""
def add(a,b):
    print('add',a,'and',b)
    print('%d+%d=' %(a,b), a+b)
    return a, b, a+b
print(add(3,4))
print(add(a=4,b=3)) #매개변수랑 인자랑 순서 바꿔서 하고 싶을 때.
"""

"""
#result=add(3,4)
A,B,result=add(3,4) #여러개로 나눠서 받을 수 있다.

print("result :", A)
print("result :", B)
print("result :", result,"\n---------------------")
"""
"""
def hello():
    print("hello")

print('reHello')
reHello=hello()
print('reHello =', reHello)
print('reHello ends')
"""
"""
def book(name,age,book1,book2):
    print(name,age,book1,book2)
    return name
"""
"""
def book(name,age,*book):
    print(name,age,end=' ')
    for i in book:
        print(i,end=' ')
    print()
    return name


name1=book('name1','100','C','C++')
print('name1: ',name1)
name2=book('name2','100','C','C++','Python') #첫번째 book function에서는 error. 매개변수 개수가 다름.
print('name2: ',name2)

i_l=(lambda x,y:x+y)(3,4)
print(i_l)
"""
"""lambda 함수와 아래 함수는 동일함
def SUM(x,y):
    return x+y
print(SUM(3,4))
"""

