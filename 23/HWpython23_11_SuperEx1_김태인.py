class InheritParent:
  def __init__(self):
    self.vl01=20 #mv생성자 초기화
  def mView(self):
    print("부모 메서드 확인")

class InheritChild(InheritParent):
  def mView(self):
    super().mView()
    print("자식 메서드 확인")

obj=InheritChild()
print(obj.vl01)
obj.mView()