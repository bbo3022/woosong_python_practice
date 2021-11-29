##Loop Lists
#연습1(CollectionType_item)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
 #for 문 뒤에는 리스트가 올 수 있다.

 #연습2(index_len().range())
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  #range()와 len()을 사용해 반복문을 사용 할 수 있다

#연습3(while_len() 비교 증감)
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#while을 사용해 루프를 돌린다. 이 떄 len으로 길이를 지정해주고 i로 인덱스를 해준다.(i는1씩 증가)

#연습4(표현식 for__ if)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#표현식.

##List Comprehension
#연습1(for__if)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#fruits를 돌려서 요소들중 a가 있는 요소는 newlist에 담아라.

#연습2(연습1을 표현식으로)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#※newlist = [expression for item in iterable if condition == True]


#연습3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
#fruits 리스트 중에서 apple이 아닌 것만 newlist에 담아라

#연습4(range(10))
newlist = [x for x in range(10)]

print(newlist)
#범위를 10까지 돌려라(10을 제외)0_9 까지 출력

#연습5(range(10),if)
newlist = [x for x in range(10) if x < 5]

print(newlist)
#10까지 돌리지만 5보다 작은것을 담아라

#연습6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
#fruits안의 요소들을 대문자로.

#연습7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)
#fruits안의 요소들을 hello로 바꿔라


#연습8
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
#fruits안의 요소들은 담는데, 바나나가 있다면 그것은 오렌지로 대체해라.