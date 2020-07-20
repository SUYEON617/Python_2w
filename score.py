#! /usr/bin/env python

a=int(input("몇 점인가요? :"))

#if (a>100 or a<0):
#    print("error")
#elif (100>=a>89):
#    print("A학점입니다.")
#elif (a>79):
#    print("B학점입니다.")
#elif (a>69):
#    print("C학점입니다.")
#elif (a>59):
#    print("D학점입니다.")
#else:
#    print("F 학점입니다.")

if (a>100 or a<0):
    print("error")
else:    
    if (a>89):
        grade="A"
    else:
        if (a>79):
            grade="B"
        else:
            if (a>69):
                grade="C"
            else:
                grade="D"
    print(grade,"학점입니다.")
