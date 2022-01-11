menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]


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

    
#-----------------------------------------------------------------------------------------
def DBset():
  try:
    file=open("./../dataSet03Bank/BankMSDB01.txt","r",encoding="utf-8")
  except FileNotFoundError:
    file=open("./../dataSet03Bank/BankMSDB01.txt","w",encoding="utf-8")
    file=open("./../dataSet03Bank/BankMSDB01.txt","r",encoding="utf-8")
  finally:
    DBdata = file.readlines()
    file.close()
  for x in range(len(DBdata)):
    DBdata[x]=DBdata[x].strip().split(",")
  return DBdata
def menuList():
  openMoney=[]

  print("="*27,"은행관리 프로그램 V01","="*27)
  print()
  for m in range(len(menu)):
    print(f"{menu[m]}",end="\t")
  print("\n")
  print("="*77)
  print()

  for outer in range(len(DBdata)):
    for inner in range(len(DBdata[outer])-1):
      print(f"{DBdata[outer][inner]:<16}",end="")
    else:
      print(f"{int(DBdata[outer][-1]):<16}")
    openMoney.append(int(DBdata[outer][-1]))
  print()
  print("-"*77)
  print()
  print(f"총인원수 {len(DBdata)}명/ 은행잔고: {sum(openMoney):,}원")
  print("="*77)
#-----------------------------------------------------------------------------------------
def menusel():
  print()
  selec=input("\t고객 번호 입력[5번:종료/0번:고객List/9번:고객가입]:")
  if selec=="5":
    print()
    print("\t","종료하겠습니다.")
    print()
    exit()

#-----------------------------------------------------------------------------------------
while True:
  DBdata=DBset()
  menuList()
  #customList()
  menusel()
   