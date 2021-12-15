#연습1
x=['Life', 'is', 'too', 'short']
X=' '.join(x)
print(X)

#연습1-1
x=['Life', 'is', 'too', 'short']
for X in x:
	print(X,end=" ")
print()


#연습2
a=(1,2,3)
b = list(a)
b.append(4)
c = tuple(b)
print(c)


#연습3
a = {'A':90, 'B':80, 'C':70}

print(a.pop("B"))


#연습4
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
A=set(a)
a=list(A)
print(a)

#연습5
a = [1, 2, 3]
a=b
a[1] = 4
c=b.copy()
c[1]=7
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
#같은 주소값을 받아오기 때문에 a의 벨류를 수정해도 b까지 변하게 된다.