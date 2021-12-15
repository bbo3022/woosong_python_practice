#Loop Dictionareis, Copy

#연습1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
#for...in.. 을 통해 키값을 가져올수 있다

#연습2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
#for.. in... 을 통해 가져온 값 중 벨류 값을 보고 싶을 땐 print(a[x])로 하면 됨

#연습3
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
#위의 방식.values()으로도 벨류값을 불러 올 수 있다

#연습4
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
#.keys()를 통해 for문 돌리면 키값이 출력

#연습5
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#.items()를 통해 for문을 돌리면 키값과 벨류를 동시에 가져와서 두가지 변수로 출력

#연습1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#.copy()로 dict 카피 가능.

#연습2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#dict()를 통해 카피가 가능


