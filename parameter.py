#! /usr/bin/env python

def test(**key):
    print(key)

test(a=1)
test(name='foo',age=3)

#왼쪽을 key값, 오른쪽을 value값으로 딕셔너리에 저장.
