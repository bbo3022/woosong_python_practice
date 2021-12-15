menu    = ['1.회원가입', '2.로그인', '3.회원목록','4.정보수정','5.회원탈퇴', '9.메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
userList=[]
temp=[]
loginInfo=[]
print(menuChk)

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
		if len(userList)==0:
			print()
			print("{0:>25}".format("먼저 회원가입해주세요"))
			print()
		else:
			print("\t\t","^Log in !")
			print()
			print()
			for signIn in range(2):
				print(f"\t{itemList[signIn]}:",end="")
				templist=input()
				temp.append(templist)
			chkMem=0
			for idx in range(len(userList)):
				if temp[0] == userList[idx][0]:
					chkMem=1
					break
			if chkMem==1:
				if temp[1]==userList[idx][1]:
					print("{0:>25}".format("로그인 성공"))
					print()
					print()
				elif userList[idx][1]!=temp[1]:
					print("{0:>25}".format("비번확인"))
					print()
					print()
			elif temp[0] != userList[idx][0]:
				print("{0:>25}".format("아이디 확인"))
				print()
				print()

					
					
			temp=[]
			
			
				
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

	elif num=="4":
		if len(userList)==0:
			print()
			print("{0:>25}".format("먼저 회원가입해주세요"))
			print()
		else:
			print("\t\t","^회원 정보 수정")
			print()
			print()
			for signIn in range(2):
				print(f"\t{itemList[signIn]}:",end="")
				templist=input()
				temp.append(templist)
			chkMem=0
			for idx in range(len(userList)):
				if temp[0] == userList[idx][0]:
					chkMem=1
					break
			if chkMem==1:
				if temp[1]==userList[idx][1]:
					print()
					print()
					print(f"\t\t{temp[0]}님 회원 수정 가능한 상태 입니다.")
					print()
					print("\t", '수정 전 내용',userList[idx])
					print()
					for memUp in range(len(itemList)):
						print(f"\t{itemList[memUp+1]:>10} 바꾸시겠습니까?(Y/N):",end="") 
						answer=input()
						answer.lower()
						if answer == "y":
							for newInfo in range(1,len(itemList)):
								print(f"\t바꿀{itemList[newInfo]} 입력:",end="") 
								answer2=input()
								userList[idx][idx+1] = answer2
								print(userList[idx]) 
				elif userList[idx][1]!=temp[1]:
					print("{0:>25}".format("비번확인"))
					print()
					print()
			elif temp[0] != userList[idx][0]:
				print("{0:>25}".format("아이디 확인"))
				print()
				print()

					
					
			temp=[]

	elif num=="5":
		if len(userList)==0:
			print()
			print("{0:>25}".format("먼저 회원가입해주세요"))
			print()
		else:
			print("\t\t","^회원탈퇴")
			print()
			print()
			for signIn in range(2):
				print(f"\t{itemList[signIn]} :",end="")
				templist=input()
				temp.append(templist)
			chkMem=0
			for idx in range(len(userList)):
				if temp[0] == userList[idx][0]:
					chkMem=1
					break
			if chkMem==1:
				if temp[1]==userList[idx][1]:
					print("{0:>25}".format("탈퇴 성공"))
					del userList[idx]
					
					print()
					print()
				elif userList[idx][1]!=temp[1]:
					print("{0:>25}".format("비번확인"))
					print()
					print()
			elif temp[0] != userList[idx][0]:
				print("{0:>25}".format("아이디 확인"))
				print()
				print()

					
					
			temp=[]
	else:
		print("\t""다시 입력해주세요")
		print()