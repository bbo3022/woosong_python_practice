money=int(input('Money를 입력:'))
card=eval(input('True/False를 입력:'))

if money >=3000 or card:
	print('택시타라')
else:
	print('걸어가세여')

print(type(card))