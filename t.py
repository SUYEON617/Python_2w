#! /usr/bin/env python


d_fruit={'price':1000,'name':'apple','tree':'apple tree'}
print(d_fruit.keys())
w=input("무엇을 찾을까요? : ")
print(d_fruit[str(w)])


STR='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'

print(STR[22:28], STR[97:103])

age =str(input("age:"))
print("Hi, I\'m %s years old" % age)
print("Hi {2}, I\'m {0} years old {1}".format(age, 3, "apple"))
print("hi, I\'m %d years old, %s " % (3,'hey'))
