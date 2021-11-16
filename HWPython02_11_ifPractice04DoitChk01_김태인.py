'''
01.  money 변수에 True 또는 False입력받는다.
sample run] money  확인 Ex. True 또는 False
-money 타입 확인
택시 사용 가능/걸어단다.
'''

money=input('True/False:')
print(type(money))
if money=='True':
	print(" 택시 사용 가능")
elif money=='False':
	print("걸어가")