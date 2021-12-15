menu    = ['1.회원가입', '2.로그인', '3.회원목록','4.정보수정','5.회원탈퇴', '9.메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList=[]
temp=[]
loginInfo=[]

for menu2 in range(len(menu)):
	menuChk.append(menu[menu2][0])
print(menuChk)


#메뉴타이틀-------------------------------------------------------------------------------------
def menuList():
	print("="*27,"메뉴선택","="*27)
	print()
	for m in menu:
		print(m, end=" ")
	print("\n")
	print("="*64)
	print()

#메뉴선택-------------------------------------------------------------------------------------
def menuSelect():
	num=0
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	if num in menuChk:
		return num
	else:
		print("\t""다시 입력해주세요")
		print()

#1번 회원가입--------------------------------------------------------------------------
def memIns():
	temp=[]	
	try:
		file=open("./../_dateSet02Mem/MemV03.txt","r")
	except FileNotFoundError:
		file=open("./../_dateSet02Mem/MemV03.txt","a")
		file=open("./../_dateSet02Mem/MemV03.txt","r")
	else:
			line=file.readlines()
	finally:
		file.close()
	dupChk=0
	print("\t\t","^SignUp !")
	print()
	# file=open("./../_dateSet02Mem/MemV03.txt","r")

	for signUp in itemList:
		print(f"\t{signUp:<10}:",end="") 
		templist=input()
		temp.append(templist)
	# userList.append(temp)
	# file=open("./../_dateSet02Mem/MemV03.txt","w")
		for i in range(len(line)):
			if line[i].split(",")[0]==temp[0]:
				dupChk=1
				break #이게 없으면 중복된 걸 찾아도 끝까지 돌아감.
	if dupChk==0:
		file=open("./../_dateSet02Mem/MemV03.txt","a")
		mem03=",".join(temp)+"\n"
		file.write(mem03)
		file.close()
		print(f"현재 회원수는 {len(line)+1}명 입니다.")
	elif dupChk==1:
		print("중복아이디가 있습니다.")	
	

#2번-------------------------------------------------------------------------------------------
def memLog():
	temp=[]
	file=open("./../_dateSet02Mem/MemV03.txt","r")
	line=file.readlines()
	if len(line)==0:
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
		for idx in range(len(line)):
			if temp[0] == line[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==line[idx][1]:
				print("{0:>25}".format("로그인 성공"))
				print()
				print()
			elif line[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != line[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
	

#3번 memSel()-------------------------------------------------------------------------------------------
def memList():
	try:
		file=open("./../_dateSet02Mem/MemV03.txt","r")
		line=file.readlines()
		if not line:
			raise FileNotFoundError()
	except:
		file=open("./../_dateSet02Mem/MemV03.txt","r")
	file.close()
	print("\t\t","^Member List !")
	if len(line)==0:
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
		for x in line:
			for y in x:
				print(f"{y}", end='')
			print()
print()

#9번-------------------------------------------------------------------------------------------
def memExit():
	print("\t""9. 메뉴를 종료합니다")
	print()

#4번-------------------------------------------------------------------------------------------
def memUpd():
	temp=[]
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
					answer=input().lower()
					if answer == "y":
						for newInfo in range(1,len(itemList)):
							print(f"\t바꿀{itemList[memUp+1]} 입력:",end="") 
							answer2=input()
							(userList[newInfo][newInfo+1])=answer2
							print(userList[idx]) 
							break
							
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
		

#5번--------------------------------------------------------------------------------------------
def memDel():
	temp=[]
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
		
#메뉴타이틀 반복-------------------------------------------------------------------------------
while True:
	menuList()
	num=menuSelect()

#1번입력-------------------------------------------------------------------------------------
	if num=="1":
		memIns()

#2번입력-------------------------------------------------------------------------------------
	elif num=="2":
		memLog()

#3번입력-------------------------------------------------------------------------------------
	elif num=="3":
		memList()
#4번입력-------------------------------------------------------------------------------------
	elif num=="4":
		memUpd()
		
#5번입력-------------------------------------------------------------------------------------
	elif num=="5":
		memDel()
		
#9번입력-------------------------------------------------------------------------------------
	elif num=="9":
		memExit()
		break

