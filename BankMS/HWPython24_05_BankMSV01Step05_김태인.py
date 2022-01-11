menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
funGetList=["getId()","getName()","getNumber()","getBalance()"]

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
      print(f"{self.AccDtoList[idx].getId():^19}{self.AccDtoList[idx].getName():^22}{self.AccDtoList[idx].getNumber():^20}{int(self.AccDtoList[idx].getBalance()):^22,}")
    print("-"*83)
    print()
    print(f"\t\t총인원수 {len(self.AccDtoList)}명/ 은행잔고: {daoObj.AccDtoList[0].bankBalance:,}원")
    print()
    print("="*83)
#----------------------------------------------------------------------------------------------
  def customInfo(self):
    print()
    selec=input("\t\t고객 번호 입력[5번:종료  /  0번:고객List  /  9번:고객가입]").strip()
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
      print(f"\t\t메뉴 번호 확인 해주세요.")
#----------------------------------------------------------------------------------------------  
  def customIns(self):
    self.temp=[0,0,0,0]
    _add=int(self.AccDtoList[len(self.AccDtoList)-1].getId()[4:])+1
    userId="{0:0>3}".format(str(_add))
    _add1=int(self.AccDtoList[len(self.AccDtoList)-1].getNumber()[8:])+1
    userNumber="{0:0>3}".format(str(_add1))
    print(self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId, self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber)
    self.newName=input("고객이름:")
    self.newMoney=input("초기입금:")
    self.temp[0]=self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId
    self.temp[1]=self.newName
    self.temp[2]=self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber
    self.temp[3]=self.newMoney

    print(self.temp)
    self.AccDtoList.append(AccountV01DTO(self.temp[0],self.temp[1],self.temp[2],self.temp[3]))
    AccountV01DTO.bankBalance+=int(self.temp[3])
    print(f"{self.temp[0]} 가입확인")
    self.file1=open("./../dataSet03Bank/BankMSDB01.txt","a",encoding="utf-8")
    tempWrite=",".join(self.temp)+"\n"
    self.file1.write(tempWrite)
    self.file1.close()
 
 #----------------------------------------------------------------------------------------------   
daoObj=AccountV01DAO()
daoObj.DBSet()
print(f"{len(daoObj.AccDtoList)}개")
print(daoObj.AccDtoList[0].getId())
print(daoObj.AccDtoList[0].bankBalance)
daoObj.customSel()
while True:
  daoObj.customInfo()
