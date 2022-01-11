menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
submenu=["입금","출금","고객정보확인","고객 탈퇴","종료"]

class AccountV01DTO:
	bankBalance=100000
	def __init__(self, customId, customName ,customNumber, customBalance):
		self.customId=customId
		self.customName=customName
		self.customNumber=customNumber
		self.customBalance=customBalance

	def getId(self):
		return self.customId
	def getName(self):
		return self.customName
	def getNumber(self):
		return self.customNumber
	def getBalance(self):
		return self.customBalance
			
	def SetId(self, customId):
		self.customId=customId
	def SetName(self, customName):
		self.customName=customName
	def SetNumber(self, customNumber):
		self.customNumber=customNumber
	def SetBalance(self, customBalance):
		self.customBalance=customBalance

#----------------------------------------------------------------------------------------------
class AccountV01DAO:
	def __init__(self):
		self.AccDtoList=[]
		self.tempList=[]
#----------------------------------------------------------------------------------------------
	def DBSet(self):
		try:
			file=open("./../dataSet03Bank/BankMSDB01.txt","r",encoding="utf-8")
		except FileNotFoundError:
			file=open("./../dataSet03Bank/BankMSDB01.txt","w",encoding="utf-8")
			file=open("./../dataSet03Bank/BankMSDB01.txt","r",encoding="utf-8")
		finally:
			bankFile = file.readlines()
			file.close()
		for idx in range(len(bankFile)):
			self.tempList=bankFile[idx].strip().split(",")
			self.AccDtoList.append(AccountV01DTO(self.tempList[0],self.tempList[1],self.tempList[2],self.tempList[3]))
			AccountV01DTO.bankBalance+=int(self.AccDtoList[idx].getBalance())

#----------------------------------------------------------------------------------------------
	def customSel(self):
		print("="*30,"은행 관리 프로그램V01","="*30)
		print()
		for m in menu:    
			print(f"{m:^15}", end="   ")
		print("\n")
		print("="*83)
		self.IdChk=[]
		for idx in range(len(self.AccDtoList)):
			print("     ",self.AccDtoList[idx].getId(),"\t\t",end="")
			print("   ",self.AccDtoList[idx].getName(),"\t\t",end="")
			print(self.AccDtoList[idx].getNumber(),"\t\t",end="")
			print(int(self.AccDtoList[idx].getBalance()),"\t",end="\n")
			self.IdChk.append(self.AccDtoList[idx].getId())
		print("-"*83)
		print()
		print(f"\t\t총인원수 {len(self.AccDtoList)}명/ 은행잔고: {AccountV01DTO.bankBalance:,}원")
		print()
		print("="*83)

#----------------------------------------------------------------------------------------------
	def customInfo(self):
		print()
		selec=input("\t고객 번호 입력[5번:종료  /  0번:고객List  /  9번:고객가입] : ")
		print()
		if selec=="5":
			print()
			print(f"\t\t시스템을 종료합니다.")
			print()
			exit()
		elif selec=="0":
			print()
			self.customSel()
			print()
			return
		elif selec=="9":
			self.customIns()
			return
		else:
			if selec in self.IdChk:
				self.customChk(selec)
			else:
				print(f"\t\t존재하지 않는 고객입니다.")

#----------------------------------------------------------------------------------------------
	def customIns(self):
		CI = int(self.AccDtoList[len(self.AccDtoList)-1].getId()[-3:])+1
		CN = int(self.AccDtoList[len(self.AccDtoList)-1].getNumber()[-3:])+1
		if CI < 10 and CI > 0:
			newCI = f'CUST00{CI}'
		elif CI < 100 and CI >=10 :
			newCI = f'CUST0{CI}'
		elif CI >=100:
			newCI = f'CUST{CI}'
		if CN < 10 and CN > 0:
			newCN = f'17-0724-00{CN}'
		elif CN < 100 and CN >=10 :
			newCN = f'17-0724-0{CN}'
		elif CN >=100:
			newCN = f'17-0724-{CN}'
		print("\t\t\t",newCI, newCN)
		c_name = input("\t\t\t고객이름 : ").strip()
		c_bal = input("\t\t\t초기입금 : ").strip()
		arr = [newCI,c_name,newCN,c_bal]
		print(arr)
		self.AccDtoList.append(AccountV01DTO(arr[0],arr[1],arr[2],arr[3]))
		AccountV01DTO.bankBalance +=int(c_bal)
		f = open("./../dataSet03Bank/BankMSDB01.txt",'a',encoding='utf-8')
		tempwrite =",".join(arr)+"\n"
		f.write(tempwrite)
		f.close()

#---------------------------------------------------------------------------------------------- 
	def customChk(self,selec):
		self.sub_customInS(selec)
		for idx in range(len(self.AccDtoList)):
				idx=idx
		while True:
			print()
			sub_selec=input("\t\t\t>>선택:")
			if sub_selec=="5":
				print("submenu종료")
				break
			elif sub_selec == '1':
				pass
				# self.customDeposit(selec)
			elif sub_selec == '2':
				print("\t2. 출금알고리즘 Chk")
			elif sub_selec == '3':
				self.sub_customInS(selec)
			elif sub_selec == '4':
				self.customDel(selec)
				if self.c_number == selec:
					break
			else:
				print("\t\t\t","다시입력해주세요")

#----------------------------------------------------------------------------------------------
	def sub_customInS(self,selec):
		print("*"*83)
		print()
		print(f'\t\t\t\t{selec} 님 계좌')
		print()
		print("*"*83)
		for x in range(len(self.AccDtoList)):
			if self.AccDtoList[x].getId() == selec:
				print()
				print("\t\t\t","고객번호:  ",self.AccDtoList[x].getId(),"\t")
				print("\t\t\t","고객이름:  ",self.AccDtoList[x].getName(),"\t\t")
				print("\t\t\t","계좌번호:  ",self.AccDtoList[x].getNumber(),"\t")
				print("\t\t\t","고객잔액:  ",self.AccDtoList[x].getBalance(),"\t")
				print()
		print("*"*83)
		print()
		print("\t\t\t\t<<< 선택하세요>>>")
		print()
		print("\t\t\t\t1. 입금")
		print("\t\t\t\t2. 출금")
		print("\t\t\t\t3. 고객정보확인")
		print("\t\t\t\t4. 고객 탈퇴")
		print("\t\t\t\t5. 종료")
		print()
#----------------------------------------------------------------------------------------------

	def customDel(self,selec):  
		self.c_number = input("\t\t\t고객번호 확인 : ")
		if self.c_number == selec:
			for idx in range(len(self.AccDtoList)):
				if self.c_number == self.AccDtoList[idx].getId():
					AccountV01DTO.bankBalance -= int(self.AccDtoList[idx].getBalance())
					#del self.AccDtoList[x]
					a = self.AccDtoList.pop(idx)
					print("\t\t\t", a.getName(),"회원탈퇴 성공!!")
					f = open("./../dataSet03Bank/BankMSDB01.txt",'r',encoding='utf-8')
					data = f.readlines()
					f = open("./../dataSet03Bank/BankMSDB01.txt",'w',encoding='utf-8')
					del data[idx]
					f.writelines(data)
					f.close()
				
					break
		else:
			print("\t\t\t^고객번호가 일치 하지 않습니다 !")

#----------------------------------------------------------------------------------------------   

	# def customDeposit(self,idx):
	# 		print("입금을 선택하셨습니다.")
	# 		putmoney=int(input("금액 입금해주세요(0:취소):"))
	# 		if putmoney==0:
	# 				print("입금취소")
	# 				return
	# 		elif putmoney<0:
	# 				print("금액 확인")
	# 		else:
	# 				a=str(int(self.AccDtoList[idx].getBalance())+putmoney)
	# 				print(a)
					
					
#----------------------------------------------------------------------------------------------   
daoObj=AccountV01DAO()
daoObj.DBSet()
daoObj.customSel()
while True:
	daoObj.customInfo()