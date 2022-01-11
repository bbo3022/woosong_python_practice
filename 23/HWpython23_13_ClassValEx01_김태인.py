class ClassValChk:
  vl=10
  def __init__(self):
    self.mv01=10

obj01=ClassValChk()
obj02=ClassValChk()
obj03=ClassValChk()

obj01.mv01+=10
print(obj01.mv01)
ClassValChk.vl+=10
print(obj01.vl, ClassValChk.vl)
obj02.mv01+=10
print(obj02.mv01)
ClassValChk.vl+=10
print(obj02.vl,ClassValChk.vl)
obj03.mv01+=10
print(obj03.mv01)
ClassValChk.vl+=10
print(obj03.vl,ClassValChk.vl)