try:
	print(100/0)

except ZeroDivisionError:
	print("ZeroDivisionError 발생 확인")
else:
	print("에러 없습니다.")
finally:
	print("예외 발생 상관없이 실행 확인")