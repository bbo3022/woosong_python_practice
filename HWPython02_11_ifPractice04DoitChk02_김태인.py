'''
02.만약 3000원 이상의 돈을 가지고 있으면
택시를 타고 그렇지 않으면 걸어가라.
-money 변수에 금액을 입력받는다. 
'''

money=int(input("금액을 입력하세요:"))
card=bool(input('True/False:'))

#False:card=0/True:card=1
print(type(card))
print(card)
card=1

if money >= 3000 or card:
	print("택시를 타라")
else:
	print("걸어가라")