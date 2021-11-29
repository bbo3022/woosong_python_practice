result01=[1,2,3]
result02=[1,2,3]

print(id(result01))
print(id(result02))

result03=result01

print(id(result01))
print(id(result03))

#result03=result01이렇게만 하면 카피가 아니라 주소값이 같아짐.

print('='*30)
result04=result01.copy()
print(id(result01))
print(id(result04))
#결과를 출력해보면 주소값이 달라진게 보인다. 카피를 하려면 이렇게!

print('='*30)
result05=list([1,2,3])
result06=list([1,2,3])
print(id(result05))
print(id(result06))
#list()를 사용해 만들어도 주소값이 달라지는것을 볼 수 있다. 