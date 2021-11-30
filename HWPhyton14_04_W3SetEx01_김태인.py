'''
** Set items are unchangeable, but you can remove items and add new items.

'''
#연습1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#순서가 없기 때문에 출력할 때마다 요소들의 순서가 바뀜

#연습2
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#len 사용 가능

#연습3
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#문자 불린 숫자 등 모든 타입 가능

#연습4
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#한 세트 안에 여러 타입을 같이 넣어도 가능

#연습5
myset = {"apple", "banana", "cherry"}
print(type(myset))
#클래스는 set이다

#연습6
thisset = set(("apple", "banana", "cherry")) 
print(thisset)
#set() 를 사용해 set을 만드는 것도 가능