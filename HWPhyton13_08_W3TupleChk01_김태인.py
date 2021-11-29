'''
Python Tuple

01. round brakets.
02. multiple items in a single variable.
03. Unchangeable
04. Oredered. Duplicates
'''

#연습1

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#튜플은 소괄호()를 사용한다

#연습2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#튜플은 요소가 중복돼도 괜찮다.

#연습3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#len 사용할 수 있다.

#연습4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#튜플 사용 시 요소가 "하나"라면 뒤에 콤마를 붙여야 튜플로 인식된다.

#연습5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#튜플은 문자, int, boolean 모두 가능

#연습6
tuple1 = ("abc", 34, True, 40, "male")
#타입이 섞여도 괜찮다.

#연습7
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#튜플은 생성자를 사용하여 튜플을 만드는 것도 가능