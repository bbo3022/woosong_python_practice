class Employee():
  def __init__(self, no, name, initday):
    self.no=no
    self.name=name
    self.initday=initday
  def payChk(self):
    return 0


class Regular(Employee):
  def __init__(self, no, name, initday,pay):
    super().__init__(no, name, initday )
    self.pay=pay
  def payChk(self):
      return self.pay

class Daily(Employee):
  def __init__(self, no, name, initday,workday,dailypay):
    super().__init__(no, name, initday)
    self.workday=workday
    self.dailypay=dailypay
  def payChk(self):
    return self.workday*self.dailypay
      
regobj01=Regular('r001','오렌지','2021-10-11',200)
dayobj01=Daily('d001','소나무','2021-10-29',9,20)

print('사번 성명 입사일 급여')
print(regobj01.no, regobj01.name, regobj01.initday, regobj01.payChk())
print(dayobj01.no, dayobj01.name, dayobj01.initday, dayobj01.payChk())