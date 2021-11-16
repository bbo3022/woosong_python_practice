'''
03.돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.
money 변수에 금액입력/card 변수에 True/False 입력 받는다.
-택시를 타고 그렇지 않으면 걸어가라.
'''

money=int(input("금액입력:"))

card=int(input("카드소유:"))
card=True

if money >=3000 or card:
	print("택시를 타라")
else:
	print("걸어가")