#문자열은 immutable.

a='pithon'
print(a[1])

#a[1]='y' 이렇게 넣으면 오류남!

print(a[:1]+'y'+a[2:])
print(a) #a값을 초기화 하지 않았기 때문에 여전히 pithon으로 출력

#python으로 출력하고싶으면
a=a[:1]+'y'+a[2:]
print(a)