
i=0
num=0

fruit = ["orange", "strawberry", "peach", "mango", "grape"]
price = ["1000원", "2500원", "1500원", "2000원", "2000원"]

print('*'*6,'과일 판매머신 V01', '*'*6)

for i in range(len(fruit)):
   print("%d . %s  :  %s" % (i+1, fruit[i], price[i]))
print((len(fruit)+1), ".", "종료")
print('='*35)

num=int(input("번호를 입력하세요 (1~6): "))
if num == 1:
   print("%s는 %s입니다." % (fruit[0], price[0]))
elif num == 2:
   print("%s는 %s입니다." % (fruit[1], price[1]))
elif num == 3:
   print("%s는 %s입니다." % (fruit[2], price[2]))
elif num == 4:
   print("%s는 %s입니다." % (fruit[3], price[3]))
elif num == 5:
   print("%s는 %s입니다." % (fruit[4], price[4]))
else:
   print("종료합니다")

"""
menu=['orange', 'strawberry', 'peach','mango','grape','종료']
price=['1000','2500','1500','2000','2000']

while True:
	print('*'*6,'우송 대학교 과일 판매머신 V01', '*'*6)
	#----------------------------------
	idx=0
	while True:
		if(idx==len(menu)-1):
			print('%d. %s '%(idx+1, menu[idx]))
			break

		print('%d.%s:%s원'%(idx+1, menu[idx], price[idx]))
		idx+=1
		break

	print('='*30)
	#----------------------------------

num=int(input('구매번호를 입력하세요 (1~6):'))


if num<len(menu):
	print('%s는 :%d원 입니다. \n'%(menu[num-1],price[num-1]))
elif num==len(menu):
	print("종료하겠습니다")
else:
	print("잘못 입력하셨습니다.")
print('='*30)
"""