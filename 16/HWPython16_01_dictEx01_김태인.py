## Python Dictionaries

#01. Key:value pairs, curly brakets,
#02. 3.7, Dictionaries are odered/but 3.6 and earlier, doctionaries are unodered.

#연습1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#dictionaries의 기본 형태는 이렇게 키값을 갖는다.

#연습2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#키값을 프린트 하면 벨류 값이 출력됨

#연습3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#키값이 중복되면 오버라이트 돼서 가장 최종에 쓰여진 키값으로 출력됨

#연습4
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#dictionaries 안에는 어떤 타입도 담을수 있다.

#연습5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#dictionaries의 타입은 'dict'로 출력