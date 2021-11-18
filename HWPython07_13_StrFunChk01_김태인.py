#문제 갯수 세기(count)
a="hobby"

print(a.count('b'))
print(len(a))#>>>이거는 길이

#위치 알려주기1(find)
a='python is the best choice'
print(a.find('b'))
print(a.find('l'))#>>>없는 거는 -1로 보여줌

#위치 알려주기2(index)
a='Life is too short'
print(a.index('t'))
print(a.index('k'))#>>>find와 달리 없는 거는 에러로