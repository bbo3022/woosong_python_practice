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
      
regobj01=Regular('r001','오렌지','2021-10-11',200)
dayobj01=Daily('d001','소나무','2021-10-29',9,20)

print('사번 성명 입사일 급여')
print(regobj01.getNo(), regobj01.getName(), regobj01.getInitday(), regobj01.payChk())
print(dayobj01.getNo(), dayobj01.getName(), dayobj01.getInitday(), dayobj01.payChk())