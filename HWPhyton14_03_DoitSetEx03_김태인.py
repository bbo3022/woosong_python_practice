#집합 자료형 관련 함수들

#값 1개 추가하기(add)-항목
s1=set([1,2,3])
s1.add(4)
print(s1)
print("="*30)
#값 여러개 추가하기(update)_Iterable
s1=set([1,2,3])
s1.update([4,5,6,3,6])
print(s1)
#3,6은 중복되기 떄문에 두번 나오지 않음/세트에선 중복이 허용되지 않기 때문에
print("="*30)
#특정 값 제거하기(remove)_항목
s1=set([1,2,3])
s1.remove(2)
print(s1)