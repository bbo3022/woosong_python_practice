#Access Items
#연습1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# 세트는 오더가 없기 때문에  인덱스 접근 할 수 없다. 그러나 for문을 사용하면 요소 하나하나 구체적으로 접근 가능

#연습2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#in 연산자도 가능

#Python - Add Set Items
#연습1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#add를 사용해 요소를 추가 할 수 있다/단 add는 한 항목 추가 할 떄 사용

#연습2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#update를 사용해 세트에 세트를 추가 할 수 있다.

#연습3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#업데이트 사용시 추가 될 것은 굳이 세트 일 필요는 없다.

#Remove Set Items
#연습1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
#thisset.remove("orange")
print(thisset)
#요소를 지울 떈 remove를 사용함/만약 세트에 없는 요소를 지우려고 하면 오류발생

#연습2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
#thisset.discard("orange")
print(thisset)
#discard로도 지울수 있다/이 경우 원래 세트에 없던 요소를 지우려고 했을 떄 오류 발생하지 않는다.

#연습3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#pop으로 요소를 꺼낼 수 있다. pop은 반환값을 받는다.

#연습4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#클리어를 통해 요소 전체를 지울 수 있다/컨테이너는 남음

#연습5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#del을 통해 지우면 컨테이너도 지워짐.