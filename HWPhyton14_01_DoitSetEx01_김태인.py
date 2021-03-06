'''
##집합 자료형
	- 중복제거
	- 교집합, 합집합, 차집합 구하기

# 집합 자료형은 set 키워드를 사용해 만들 수 있다.
# set 자료형의 특징
# - 중복을 허용하지 않는다.
# - 순서가 없다(Unordered)

리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을
얻을 수 있지만 set 자료형은 순서가 없기 때문에 인덱싱으로 값을
얻을 수 없다.

딕셔너리 역시 순서가 없는 자료형이라 인덱싱을 지원하지 않는다.
set 자료형에 저장된 값을 인덱싱으로 접근하려면  다음과 같이 리스트나 튜플

** 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한
필터 역할로 종종 사용하기도 한다.


'''

s1=set([1,2,3])
print(s1)

print('-'*20)

s2=set("hello")
print(s2)
#set는순서가 없기 때문에 출력 순서가 매번 다르다!