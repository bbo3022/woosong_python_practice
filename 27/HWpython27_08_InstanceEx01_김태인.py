class Employee():
  def __init__(self, no, name, initday):
    self.no=no
    self.name=name
    self.initday=initday

  def payChk(self):
    return 0

  def getNo(self):
    return self.no
  def getName(self):
    return self.name
  def getInitday(self):
    return self.initday

  def setNo(self, no):
    self.no=no
  def setName(self, name):
    self.name=name
  def setInitday(self, initday):
    self.initday=initday


class Regular(Employee):
  def __init__(self, no, name, initday,pay):
    super().setNo(no)
    super().setName(name)
    super().setInitday(initday)
    self.pay=pay
  def payChk(self):
      return self.pay

class Daily(Employee):
  def __init__(self, no, name, initday,workday,dailypay):
    super().setNo(no)
    super().setName(name)
    super().setInitday(initday)
    self.workday=workday
    self.dailypay=dailypay
  def payChk(self):
    return self.workday*self.dailypay
      
#regobj01=Regular('r001','오렌지','2021-10-11',200)
#dayobj01=Daily('d001','소나무','2021-10-29',9,20)

def empTitle():
  print("="*50)
  print('사번  구분  성명    입사일  급여')
  print("="*50)

employee=[
    Regular('r001','오렌지','2021-10-11',200),
    Daily('d001','소나무','2021-10-29',9,20),
    Regular('r002','사과과','2021-10-11',200),
    Daily('d002','밤나무','2021-10-29',9,20),
    Regular('r003','딸기기','2021-10-11',200),
    Daily('d003','감나무','2021-10-29',9,20)
]

sameValList=["no","devision","name",'initday']

empTitle()
for emp in employee:
  for idx,obj in enumerate(sameValList):
    if idx==1:
      if isinstance(emp,Regular):
        print("일반직",end="  ")
      elif isinstance(emp,Daily):
        print("특수직",end="  ")
      continue
    value="emp.get"+obj[0].upper()+obj[1:]+"()"
    print(eval(value),end=" ")
  else:
    print(emp.payChk()) 
