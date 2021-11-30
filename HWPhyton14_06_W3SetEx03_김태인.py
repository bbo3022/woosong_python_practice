#Join Two Sets:몇가지 방법이 있음

#연습1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#.union을 통해 두 세트를 합칠 수 있다. 이때 반환값으로 해야 볼 수 있음

#연습2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#업데이트를 통해 세트를 합칠 수 있지만 이때는 반환값이 아닌 기준이 되는 세트로 프린트해야 볼 수 있다.

#연습3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#교집합의 업데이트도 마찬가지로 기준이 되는 x를 프린트해야 출력가능

#연습4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#intersection만 사용하면 새로운 반환값 z를 프린트 해야 볼 수 있다.

#연습5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#symmetric_difference_update도 마찬가지로 x에 담는 것이기 때문에 반환값이 없다

#연습6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
#업데이트가 없기 때문엔 반환값z로 출력값을 볼 수 있다.