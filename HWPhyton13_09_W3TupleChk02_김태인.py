#연습1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#apple
#튜플에서도 인덱스 사용 가능

#연습2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])#cherry
#네거티브 인덱스도 사용가능

#연습3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])# ("cherry", "orange", "kiwi")
#range도 사용 가능

#연습4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])# ("apple", "banana", "cherry", "orange")
#처음 범위 생략하면 처음부터

#연습5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])#("cherry", "orange", "kiwi", "melon", "mango")
#마지막 범위 생략하면 끝까지.

#연습6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])#("orange", "kiwi", "melon")
#네거티브 범위도 가능

#연습7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  #in 연산자도 사용 가능합니다.