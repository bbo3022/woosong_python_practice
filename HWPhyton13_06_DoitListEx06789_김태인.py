#리스트에 요소 추가
a=[1,2,3]
a.append(4)
print(a)#[1,2,3,4]

a.append([5,6])
print(a)#[1,2,3,4,[5,6]]
print('='*20)

#리스트 정렬
a=[1,4,3,2]
a.sort()#공백은 기본. 기본은 오름차순
print(a)#[1,2,3,4]

a=['a','c','b']
a.sort()
print(a)#[a,b,c,]
print('='*20)

#리스트 뒤집기

a=['a','c','b']
a.reverse()#sort랑 관련없음
print(a)#[b,c,a]
print('='*20)

#위치변환
a=['a','c','b']
print(a.index('b'))#2
print('='*20)


a=[1,2,3]
a.insert(0,4)
print(a)#[4,1,2,3]
a.insert(3,5)
print(a)#[4,1,2,5,3]
print('='*20)

#리스트 요소 제거
a=[1,2,3,1,2,3]
a.remove(3)#3이 두개이지만 처음 3만 지워짐
print(a)#[1,2,1,2,3]
print('='*20)

#리스트 요소 끄집어내기
a=[1,2,3]
print(a.pop())#공백으로 냅두면 마지막 요소
print(a)#[1,2]
print('='*20)

#a.pop(1)은 a[1]의 값을 끄집어 낸다.
a=[1,2,3]
a.pop(1)
print(a)#[1,3]
print('='*20)

#리스트에 포함된 요소 x의 개수 세기
a=[1,2,3,1]
print(a.count(1))#2
print('='*20)

#리스트 확장(Extend)
#extend(x)에서 x에는 리스트외 iterate 올 수 있으며 원래의 a리스트에 x리스트를 더한다.

a=[1,2,3]
a.extend((4,5))
print(a)#[1,2,3,4,5]
a.extend('nice')
print(a)#[1,2,3,'n','i','c','e']