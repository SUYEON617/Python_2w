#! /usr/bin/env python

chicken=10
people =5

def cnt_c(people):
    chicken=20
    chicken-=people
    print('cnt_c print',chicken)

def cnt_g(people):
    global chicken
    chicken-=people
    print('cnt_g print',chicken)

cnt_c(people)
cnt_g(people)
