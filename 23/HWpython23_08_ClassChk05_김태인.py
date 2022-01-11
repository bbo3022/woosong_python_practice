class CalV01:
  def __init__(self,n01,n02):
    self.num01=n01
    self.num02=n02
    
  def add(self):
   return  self.num01+self.num02

  def sub(self):
   return  self.num01-self.num02

  def mul(self):
   return  self.num01*self.num02

  def div(self):
   return  self.num01//self.num02

#덧셈객체생성
cal01=CalV01(100,20)
result1=cal01.add()

#뺄셈객체생성
cal02=CalV01(100,20)
result2=cal02.sub()

#곱셈객체생성
cal03=CalV01(100,20)
result3=cal03.mul()

#나눗셈객체생성
cal04=CalV01(100,20)
result4=cal04.div()


print(f"{cal01.num01}+{cal01.num02}={result1}")
print(f"{cal02.num01}-{cal02.num02}={result2}")
print(f"{cal03.num01}*{cal03.num02}={result3}")
print(f"{cal04.num01}/{cal04.num02}={result4}")