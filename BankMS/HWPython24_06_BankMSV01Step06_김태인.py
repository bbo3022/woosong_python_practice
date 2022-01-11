menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
funGetList=["getId()","getName()","getNumber()","getBalance()"]
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
    set.customId=customId
  def SetName(self, customName):
    set.customName=customName
  def SetNumber(self, customNumber):
    set.customNumber=customNumber
  def SetBalance(self, customBalance):
    set.customBalance=customBalance

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
    for idx in range(len(self.AccDtoList)):
      print(f"{self.AccDtoList[idx].getId():^20}{self.AccDtoList[idx].getName():>11}\t{self.AccDtoList[idx].getNumber():^27}{int(self.AccDtoList[idx].getBalance()):>12,}")
    print("-"*83)
    print()
    print(f"\t\t총인원수 {len(self.AccDtoList)}명/ 은행잔고: {AccountV01DTO.bankBalance:,}원")
    print()
    print("="*83)

#----------------------------------------------------------------------------------------------
  def customInfo(self):
    print()
    selec=input("\t고객 번호 입력[5번:종료  /  0번:고객List  /  9번:고객가입] : ").strip()
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
      print("="*83)
    elif selec=="9":
      self.customIns()
    else:
      for idx in range(len(self.AccDtoList)):
        if selec in self.AccDtoList[idx].getId:
          self.customChk
      else:
        print(f"\t\t존재하지 않는 고객입니다.")

#----------------------------------------------------------------------------------------------  
  def customIns(self):
    self.temp=[0,0,0,0]
    _add=int(self.AccDtoList[len(self.AccDtoList)-1].getId()[4:])+1
    userId="{0:0>3}".format(str(_add))
    _add1=int(self.AccDtoList[len(self.AccDtoList)-1].getNumber()[8:])+1
    userNumber="{0:0>3}".format(str(_add1))
    print("\t\t",self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId, self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber)
    print()
    self.newName=input("\t\t고객이름:")
    self.newMoney=input("\t\t초기입금:")
    self.temp[0]=self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId
    self.temp[1]=self.newName
    self.temp[2]=self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber
    self.temp[3]=self.newMoney

    print(self.temp)
    self.AccDtoList.append(AccountV01DTO(self.temp[0],self.temp[1],self.temp[2],self.temp[3]))
    AccountV01DTO.bankBalance+=int(self.temp[3])
    print(f"\t\t{self.temp[0]} 가입확인")
    self.file1=open("./../dataSet03Bank/BankMSDB01.txt","a",encoding="utf-8")
    tempWrite=",".join(self.temp)+"\n"
    self.file1.write(tempWrite)
    self.file1.close()

#----------------------------------------------------------------------------------------------  
  def customChk(self,selec):
    while True:
      self.selec=selec
      for idx in range(len(self.AccDtoList)):
        if self.selec==self.AccDtoList[idx].getId():
          vidx=idx
          break
      print("*"*83)
      print("\t\t\t\t",self.AccDtoList[vidx].getName(),"님 계좌")
      print("*"*83)
      print(f"\t\t\t{menu[0]}: {self.AccDtoList[vidx].getId()}")
      print(f"\t\t\t{menu[1]}: {self.AccDtoList[vidx].getName()}")
      print(f"\t\t\t{menu[2]}: {self.AccDtoList[vidx].getNumber()}")
      print(f"\t\t\t{menu[3]}: {self.AccDtoList[vidx].getBalance()}")
      print("*"*83)
      print("\t\t\t\t<<<선택하세요>>>")
      for idx in range(len(submenu)):
        print(f"\t\t\t{int(idx+1)}.{submenu[idx]}")
      self.subselec=input("\t\t\t\t>>>선택:")
      if self.subselec=="5":
        print("이전 메뉴로 돌아갑니다.")
        return self.customInfo()

#----------------------------------------------------------------------------------------------
  
 #----------------------------------------------------------------------------------------------   
daoObj=AccountV01DAO()
daoObj.DBSet()
daoObj.customSel()
while True:
  daoObj.customInfo()
