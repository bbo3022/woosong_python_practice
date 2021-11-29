# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds>> List ≒ Tuples ≠ Unchangeable

#연습1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#튜플은 요소 변경이 불가하다. 그러나 튜플 >> 리스트>> 요소삭제>>다시 튜플화 하는 방법으로 가능하다

#연습2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
#요소 추가도 같은 방법으로 가능

#연습3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#튜플에 요소 추가는 불가하지만 튜플에 튜플을 추가하는것은 가능하다.

#연습4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)
#요소 제거도 같은 방법으로 할 수있다. 

#연습5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 
#하지만 튜플 전체를 지우는것은 가능하다. 이 경우 오류로 출력(모두 삭제됐기 때문에)