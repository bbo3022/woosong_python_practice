#연습1(.fromkeys())

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict)
# .fromkeys(x,y)를 통해 모든 키값의 벨류를 초기화 해줄 수 있다. x엔 키값/y엔 초기화 해줄 값

#연습2(setdefault)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
#.setdefault(x,y)로 디폴트값을 줄 수 있다. 만약x가 키값중에 있으면 그 벨류를 출력하고, x가 없다면 x를 키값에 넣고 y를 벨류로 넣어라.