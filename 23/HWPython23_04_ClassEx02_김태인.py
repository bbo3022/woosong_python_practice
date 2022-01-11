class CalV01:
  def dbset(self):
    self.result=0
    
  def add(self, num):
   #global result
   self.result=self.result+num
   return  self.result

#객체생성
cal01=CalV01()
cal01.dbset()
print(cal01.add(5))
print(cal01.add(7))

#객체생성
cal02=CalV01()
cal02.dbset()
print(cal02.add(3))
print(cal02.add(4))


#객체생성
cal03=CalV01()
cal03.dbset()
print(cal03.add(10))
print(cal03.add(80))





'''
클래스:
  -객체 생성 후
  -java:new생성자, 객체자신>>this
  -생성자:모양_메소드 같다.>>클래스 이름과 같은 메소드
-----------------------------------------------------------------

객체명=생성자

'''