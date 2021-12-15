#Add items/Remove

#연습01
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#['키값']="벨류값"의 형태로 추가

#연습2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#.update({"키값":"벨류값"})업데이트 연산자 이용시에는 이 형식으로 추가

#연습3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#.pop('키값')을 사용해서 제거 가능하다.

#연습4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#.popitem()을 사용하면 가장 마지막 값이 사라짐.

#연습5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#del을 통해 데이터를 삭제 할 수 있다.

#연습6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
#또 del을 통해 데이터 모두를 지울 수 있는데 이 경우 컨테이너도 삭제되므로 에러 발생

#연습7
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict.clear()
print(thisdict)
#.clear()를 통해 데이터를 삭제하면 컨테이너는 남게 됨