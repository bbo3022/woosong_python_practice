
'''
isdisjoint()	>> 두개의 세트에 교집합인 것의 존재를 확인하는 것
issubset()	x가 Y에 완전히 존재하는지 확인
issuperset()	x에 y가 완전히 존재하는지 확인

is가 있으면 True/False로 표현됨
'''

#연습1
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#연습2
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#연습3
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
