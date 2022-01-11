menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]

class AccountV01DTO:
  bankBlance=100000
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
#-----------------------------------------------------------------------------------------
def menuList():
  print("="*27,"은행관리 프로그램 V01","="*27)
  print()
  for m in menu:
    print(m, end=" ")
  print("\n")
  print("="*73)
  print()
#-----------------------------------------------------------------------------------------
def customList():
  file=open("./../dataSet03Bank/BankMSDB01.txt","r")
  

#-----------------------------------------------------------------------------------------
while True:
  menuList()