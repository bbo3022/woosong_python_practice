class CalV01:
  def dbset(self):
    self.num01=0
    self.num02=0
    
  def add(self, num01, num02):
   self.num01=num01
   self.num02=num02
   return  self.num01+self.num02

#객체생성
cal01=CalV01()
cal01.dbset()
result=cal01.add(20,30)

print(f"{cal01.num01}+{cal01.num02}={result}")