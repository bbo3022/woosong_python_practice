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


daoObj=AccountV01DAO()
daoObj.DBSet()
print(f"{len(daoObj.AccDtoList)}개")
print(daoObj.AccDtoList[0].getId())
print(daoObj.AccDtoList[0].bankBalance)