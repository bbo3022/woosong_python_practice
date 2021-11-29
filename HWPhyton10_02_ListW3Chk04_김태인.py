#연습1(append())
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#append()를 사용해 요소를 추가할 때는 마지막 순서에 삽입 된다.

#연습2(specified index:insert())
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#insert()를 사용하면 구체적인 index를 사용해 원하는 위치에 삽입 가능하다.

#연습3(list:Extend())
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#List안에 List목록 전체는 extend()를 사용해 삽입 할 수도 있다. 

#연습4(Any CollectionType)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#List 안에 튜플이나 다른 콜렉션 타입도 삽입이 가능하다. 