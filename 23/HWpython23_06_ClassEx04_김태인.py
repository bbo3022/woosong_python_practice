class CalV01:
  def dbset(self):
    self.num01=0
    self.num02=0
    
  def add(self, num01, num02):
   self.num01=num01
   self.num02=num02
   return  self.num01+self.num02

  def sub(self, num01, num02):
   self.num01=num01
   self.num02=num02
   return  self.num01-self.num02

  def mul(self, num01, num02):
   self.num01=num01
   self.num02=num02
   return  self.num01*self.num02

  def div(self, num01, num02):
   self.num01=num01
   self.num02=num02
   return  self.num01//self.num02

#덧셈객체생성
cal01=CalV01()
cal01.dbset()
result1=cal01.add(100,20)

#뺄셈객체생성
cal02=CalV01()
cal02.dbset()
result2=cal02.sub(100,20)

#곱셈객체생성
cal03=CalV01()
cal03.dbset()
result3=cal03.mul(100,20)

#나눗셈객체생성
cal04=CalV01()
cal04.dbset()
result4=cal04.div(100,20)


print(f"{cal01.num01}+{cal01.num02}={result1}")
print(f"{cal02.num01}-{cal02.num02}={result2}")
print(f"{cal03.num01}*{cal03.num02}={result3}")
print(f"{cal04.num01}/{cal04.num02}={result4}")