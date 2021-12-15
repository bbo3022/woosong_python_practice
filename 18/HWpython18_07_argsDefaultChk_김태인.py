'''
#매개변수에 초기값 미리 설정하기

	say_myself 함수는 3개의 매개변수를 받아서
	마지막 인수인 man 이 True이면 남자, False면 여자 출력
	default값이 man이므로 아무 것도 적지 않으면 man으로 인식
'''

def say_myself(name, old, man=True):
	print("나의 이름은 %s입니다."%name)
	print("나이는 %d살 입니다."%old)

	if man:
		print("남자입니다.")
	else:
		print('여자입니다.')

say_myself("소나무",27)
print()
say_myself("오렌지",21,False)
print()
say_myself("사과",21,1)#숫자를 입력하면 True기 때문에 True로 인식
print()
say_myself("오렌지",2,man)
print()


'''
say_myself("오렌지",22,man)
으로 입력하면 오류 
man이 정의 되지 않았다고 함
즉 위에서 man을 참으로 정의했기 때문에
참, 거짓으로만 입력해야하는것
'''