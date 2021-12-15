#함수형식01: 기본함수
'''
mHello1 함수 생성_?안녕하세요
'''
def mHello1():
	print("안녕하세요")

mHello1()
mHello1()
mHello1()

#함수형식02: 매개변수>>>호출할 때 값 할당
'''
mHello2 함수 생성_? 이름값을 받아서>>OO님 안녕하세요
'''
def mHello2(vName):
	print(f"{vName}님 안녕하세요")

mHello2("홍길동")
mHello2("오렌지")

#함수형식03: return
'''
mHello3 함수 생성_?인삿말을 반환 받아서 출력
'''
def mHello3():
	return "안녕하세요"

result=mHello3()
print(result)

#함수형식04: 매개변수, return
'''
mHello4 함수 생성_이름값을 받아서 인사말과 함께 반환
'''
def mHello4(vName):
	return vName+"님 안녕하세요"

result=mHello4("홍길동")
print(result)

