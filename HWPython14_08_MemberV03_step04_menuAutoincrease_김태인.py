menu = ['1. 회원가입', '2. 로그인', '3. 회원목록','4.회원탈퇴','9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList=[]
temp=[]

for menu2 in range(len(menu)):
	menuChk.append(menu[menu2][0])
print(menuChk)

'''
다른 샘플답안
1.
for idx in menu:
	temp=idx.split('.')
	menuChk.append(temp[0])

2.
menuChk=[str(noChk) for noChk in range(1,len(menu))]
menuChk.append(str(9))
print(menuChk)
'''

while True:
	print("="*20,"메뉴선택","="*20)
	print()
	for m in menu:
		print(m, end=" ")
	print("\n")
	print("="*50)
	print()
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	print()
	if num in menuChk:
		if num=="1":
			print("\t\t","^SignUp !")
			print()
			for signUp in itemList:
				print(f"\t{signUp:<10}:",end="") 
				templist=input()
				temp.append(templist)
			userList.append(temp)
		
			for vList in userList:	
				print(vList)
			print(f"현재 회원수는 {len(userList)}명입니다")	
			print()
			#temp.clear()
			temp=[]	
			print()

		elif num=="2":
			print("\t""2. 로그인 알고리즘 chk")
			print()
		elif num=="3":
			print("\t\t","^Member List !")
			if len(userList)==0:
				print()
				print("{0:>25}".format("먼저 회원가입해주세요"))
				print()
			else:
				print('='*50)
				for a in itemList:
					print("{0:^7}".format(a), end='')
				print()
				print('='*50)
				print()
				for x in userList:
					for y in x:
						print("{0:^7}".format(y), end='')
					print()
			print()
		elif num=="9":
			print("\t""9. 메뉴를 종료합니다")
			print()
			break
	elif num != menuChk:
		print("\t""다시 입력해주세요")