##python - loop Tuples

#연습1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#튜플도 for문 사용 가능

#연습2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#인덱스 사용시 range.len 사용 가능

#연습3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#while도 사용 가능..

##Join Tuples

#연습1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#튜플 끼리의 연산은 가능하다

#연습2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#역시 *도 가능하다.
##Tuples Methods]
#연습1
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#카운트 가능

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
#인덱스도 당연히 가능
