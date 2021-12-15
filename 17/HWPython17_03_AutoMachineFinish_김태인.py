i=0
num=0

fruit = ["orange", "strawberry", "peach", "mango", "grape"]
price = [1000, 2500, 1500, 2000, 2000]


while True:
	print('*'*6,'과일 판매머신 V01', '*'*6)

	for i in range(len(fruit)):
		print("%d . %s  :  %s원" % (i+1, fruit[i], price[i]))
	print((len(fruit)+1), ".", "종료")
	print('='*35)
	
	num=int(input("번호를 입력하세요 (1~6): "))
	
	if num <= len(fruit):
		print("\n\n")
		print("입력하신 구매번호는",num,"입니다")
		print("\n\n")
		pay=int(input("금액 투입하세요:"))
		if pay < price[i]:
			print("금액이 부족합니다.")
			print("\n\n")
		elif pay>10000:
			print("금액을 확인해주세요")
		elif pay > price[i]:
			print("투입된 금액은",pay,"원 입니다")
			print('='*12,'거스름 돈','='*12)
			print("거스름 돈은",pay-price[num-1],"원 입니다.")
			change=pay-price[num-1]
			change5000= change //5000
			change-=5000*change5000
			change1000= change //1000
			change-=1000*change1000
			change500= change//500
			change-=500*change500
			change100=change //100
			change-=100*change100
			if change5000!=0:
				print(f"5000원:{change5000}장")
			if change1000!=0:
				print(f"1000원:{change1000}장")
			if change500!=0:
				print(f"500원:{change500}개")
			if change100!=0:
				print(f"100원:{change100}개")
		print('='*35)
		print('='*35)
	elif num > len(fruit):
		print("\n\n")
		print("선택지 내의 숫자를 입력하세요")
		print("\n\n")
	if num == len(fruit)+1:
		print('='*35)
		print("종료합니다")
		print('='*35)
		print("\n\n")
		break