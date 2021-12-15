#연습1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#키값으로 접근해서 벨류값을 얻을 수 있다.

#연습2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
#.get('키값')을 통해서도 똑같은 결과를 얻을 수 있다.

#연습3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#.keys()를 통해 모든 키값을 얻을 수 있다.

#연습4
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
# 키값을 추가 할 수 있다.a['추가할 키값']='추가할 벨류'

#연습5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
#.values()를 통해 벨류값들을 모두 얻어 올 수 있다.

#연습6
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#위의 방법(a['키값']='업데이트할 벨류')을 통해 벨류값도 업데이트가 가능함.

#연습7
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#a[추가할 키값]="추가할 벨류값"으로 새로운 키값과 벨류를 추가 가능

#연습8
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
#.items()를 통해 각가의 키값과 벨류를 튜플형식으로 가져온다.

#연습9
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#똑같은 방법으로 아이템의 값을 업데이트 할 수 있다.

#연습10
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#in 연산자를 통해 키값의 유무를 확인 할 수 있음