#연습1
mylist = ["apple", "banana", "cherry"]
#리스트 기본 형태

#연습2(indexed)
thislist = ["apple", "banana", "cherry"]
print(thislist)
#인덱스가 존재함

#연습3(Duplicate)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#value가 중복 가능함(index가 내부적으로 지정돼 있기 때문에.)

#연습4(len())
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#len()으로 묶게되면 길이가 나옴

#연습5(any data type)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#리스트는 문자, 숫자, boolean 모두 가능

#연습6(different data type)
list1 = ["abc", 34, True, 40, "male"]
#서도 다른 type의 value가 하나의 리스트에 있어도 가능

#연습7(type())
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#type은 List로 나온다

#연습8(Constructor)
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#list라고 따로 지정해줘도 가능 이때는 list()의 형식으로 사용